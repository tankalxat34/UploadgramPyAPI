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
    - telegrams channel: https://t.me/uploadgramme
"""

import requests, getpass, os, os.path, json

global USER_AGENT
# You can replace this user-agent any different
USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.2"


class File:
    def __init__(self, id: str, key: str):
        """
        :param id:  Get id file that placed at the end URL for file
        :param key: Key for rename and remove file from server
        """
        self.id = id
        self.key = key

        self.url = "https://dl.uploadgram.me/" + self.id
        self.url_import = None

        self.r = requests.get("https://api.uploadgram.me/get/" + self.id)
        if self.r:
            self.file = self.r.json()

            ### Create attibutes for class ###
            self.name = self.file["filename"]
            self.size = self.file["size"]
            self.userTelegramId = self.file["userTelegramId"]
            self.userIp = self.file["userIp"]

            ### Create import link ###
            dict_part_url_to_import = ({str(self.key): {'filename': os.path.basename(self.name),
                                                           'size': int(self.size),
                                                           'url': str(self.url)}})
            self.url_import = "https://uploadgram.me/upload/#import:" + json.dumps(dict_part_url_to_import)
        else:
            raise ValueError(f"File with this id ({self.id}) does not exist")

    def get_json(self):
        """
        Returns json response from answer
        """
        return self.file

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
        self.r_delete = requests.get("https://api.uploadgram.me/delete/" + self.key,
                                     headers={"user-agent": USER_AGENT})
        return self.r_delete

    def rename(self, new_name: str):
        """
        Returns response from server if file renamed successfully
        """
        self.r_rename = requests.post("https://api.uploadgram.me/rename/" + self.key,
                                      data={"new_filename": new_name,
                                            "user-agent": USER_AGENT})
        return self.r_rename


class NewFile:
    def __init__(self, path):
        """
        :param path:    Path to file what you want to upload
        """
        self.path = path
        self.url_upload = 'https://api.uploadgram.me/upload'
        self.file = open(self.path, "rb")

        self.key = None
        self.id = None
        self.url = None
        self.url_import = None

    def upload(self):
        """return {'ok': True, 'url': 'https://dl.uploadgram.me/new_file_id', 'delete': 'delete_key'}"""
        self.r = requests.post(self.url_upload,
                               headers={"user-agent": USER_AGENT},
                               files={"file_upload": self.file})
        self.key = self.r.json()["delete"]
        self.id = self.r.json()["url"].split("/")[-1]
        self.url = self.r.json()["url"]
        self.url_import = File(self.id, self.key).url_import
        return self.r.json()
