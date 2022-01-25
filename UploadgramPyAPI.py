"""
********************************
*------------------------------*
*--------UploadgramPyAPI-------*
*------------------------------*
********************************
Author: tankalxat34
Description: 
    This API can be upload, download, remove and rename any files from the service uploadgram.me. Using programming language: Python.
Contacts (API Author):
    - github: https://github.com/tankalxat34/UploadgramPyAPI
    - email: tankalxat34@gmail.com
Contacts (Uploadgram Author):
    - telegram channel: https://t.me/uploadgramme

****************************************************************
*----------------------Example of use:-------------------------*
****************************************************************

import UploadgramPyAPI

# Upload any file
up_new_file = UploadgramPyAPI.NewFile("D:\\image.jpg")
up_new_file.upload()

# Set up connection to file like here
up_file = UploadgramPyAPI.File("611e5e6237f6fg", "e3da26e9dddd2e01b8c0831370695e9088a96ff81e262fc2g")
# or like here
# up_file = UploadgramPyAPI.File("e3da26e9dddd2e01b8c0831370695e9088a96ff81e262fc2g")
# or like this
# up_file = UploadgramPyAPI.File("611e5e6237f6fg")

# Download any file
up_file.download()

# Rename any file
up_file.rename("ItsNewNameForFile.jpg")

# Delete any file
up_file.delete()

****************************************************************
"""

import requests, getpass, os, os.path, json

# You can replace this user-agent any different
global USER_AGENT
USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.2"

# If you don't want to rename or delete the file you can use this const for param "key" in class "File"
global NONE
NONE = "none"

# Const for default length of 'id' parameter
global LENGTH_ID
LENGTH_ID = 14

class UploadgramConnectionError(Exception):
    def __init__(self):
        super().__init__("uploadgram.me currently unavailable. Please, try again later.")

class UploadgramUsingKeyError(Exception):
    def __init__(self, text):
        super().__init__('You can not ' + text + ' this file because you using the NONE-const for "key" parameter or you using "id" file instead of "key" parameter')

class UploadgramFileIsNotAvalible(Exception):
    def __init__(self, id):
        super().__init__("This file " + id + " does not exists")

class File:
    def __init__(self, id, key=NONE):
        """
        :param id:  Get id file that placed at the end URL for file
        :param key: Key for rename and remove file from server
        """
        self.id = id
        if len(self.id) > LENGTH_ID:
            self.key = self.id
        else:
            self.key = key

        self.url_import = None

        try:
            self.r = requests.get("https://api.uploadgram.me/get/" + self.id)
        except requests.exceptions.ConnectionError:
            raise UploadgramConnectionError()

        if self.r:
            self.json = self.r.json()

            self.id = self.json["url"].split("/")[-1]
            self.url = "https://dl.uploadgram.me/" + self.id

            ### Create attibutes for class ###
            self.name = self.json["filename"]
            self.size = self.json["size"]

            try:
                self.userTelegramId = self.json["userTelegramId"]
            except Exception:
                self.userTelegramId = None

            try:
                self.userIp = self.json["userIp"]
            except Exception:
                self.userIp = None

            if str(self.key) != NONE and len(self.key) > LENGTH_ID:
                ### Create import link ###
                dict_part_url_to_import = ({str(self.key): {'filename': os.path.basename(self.name),
                                                               'size': int(self.size),
                                                               'url': str(self.url)}})
                self.url_import = "https://uploadgram.me/upload/#import:" + json.dumps(dict_part_url_to_import)
            else:
                self.url_import = 'UNABLE TO GENERATE url_import BECAUSE self.key GOT A STRING "none" VALUE'
        else:
            raise UploadgramFileIsNotAvalible(self.id)

    def get_json(self):
        """
        Returns json response from answer
        """
        return self.json

    def download(self, path=f"C:\\Users\\{getpass.getuser()}\\Downloads\\"):
        """
        Returns True if the file was download on your PC
        """
        with open(path + self.name, 'wb') as f:
            f.write((requests.get(self.url + "?raw")).content)
        return True

    def delete(self):
        """
        Returns response from server if file deleted successfully
        """
        if self.key != NONE:
            self.r_delete = requests.get("https://api.uploadgram.me/delete/" + self.key,
                                     headers={"user-agent": USER_AGENT})
        else:
            raise UploadgramUsingKeyError("delete")
        return self.r_delete

    def rename(self, new_name: str):
        """
        Returns response from server if file renamed successfully
        """
        if self.key != NONE:
            self.r_rename = requests.post("https://api.uploadgram.me/rename/" + self.key,
                                      data={"new_filename": new_name,
                                            "user-agent": USER_AGENT})
        else:
            raise UploadgramUsingKeyError("rename")
        return self.r_rename


class NewFile:
    def __init__(self, path):
        """
        :param path:    Path to file what you want to upload
        """
        try:
            self.check_to_avaliable = requests.get("https://api.uploadgram.me/status", headers={"user-agent": USER_AGENT})
            self.path = path
            self.url_upload = 'https://api.uploadgram.me/upload'
            self.readfile = open(self.path, "rb")

            self.key = None
            self.id = None
            self.url = None
            self.url_import = None
        except Exception:
            raise UploadgramConnectionError()

    def upload(self):
        """return {'ok': True, 'url': 'https://dl.uploadgram.me/new_file_id', 'delete': 'delete_key'}"""
        self.r = requests.post(self.url_upload,
                               headers={"user-agent": USER_AGENT},
                               files={"file_upload": self.readfile})
        self.key = self.r.json()["delete"]
        self.id = self.r.json()["url"].split("/")[-1]
        self.url = self.r.json()["url"]
        self.url_import = File(self.id, self.key).url_import
        return self.r.json()
