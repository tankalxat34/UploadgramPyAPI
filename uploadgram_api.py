"""
~~~~~~~~~~~~~~~~~~~~~
~~~~uploadgram_api.py~~~~
~~~~~~~~~~~~~~~~~~~~~

Author: tankalxat34

Description: 
    This API can be upload, download, remove and rename any files from the service uploadgram.me. Using programming language: Python.

Contacts (API Author):
    - telegram: @tankalxat34
    - telegram channel: https://t.me/tankalxat34_channel
    - github: https://github.com/tankalxat34/UploadgramPyAPI

Contacts (Uploadgram Author):
    - telegrams channel: https://t.me/uploadgramme

"""

import requests, getpass, os, os.path, fake_useragent, json

global USER_AGENT
USER_AGENT = fake_useragent.UserAgent().chrome


class UploadgramFile:
    def __init__(self, id: str, key: str):
        """
        :param id:  Get id file that placed at the end URL for file
        :param key: Key for rename and remove file from server
        """
        self.id = id
        self.key = key

        self.url = "https://api.uploadgram.me/get/"
        self.url_file = "https://dl.uploadgram.me/" + self.id
        self.url_status = 'https://api.uploadgram.me/status'
        self.url_delete = "https://api.uploadgram.me/delete/"
        self.url_import = ""

        self.r = requests.get(self.url + self.id)
        if self.r:
            self.file = self.r.json()

            ### Create attibutes for class ###
            self.name = self.file["filename"]
            self.size = self.file["size"]
            self.userTelegramId = self.file["userTelegramId"]
            self.userIp = self.file["userIp"]

            ### Create import link ###
            if self.key != None:
                dict_part_url_to_import = ({str(self.key): {'filename': os.path.basename(self.name),
                                                               'size': int(self.size),
                                                               'url': str(self.url_file)}})
                self.url_import = "https://uploadgram.me/upload/#import:" + json.dumps(dict_part_url_to_import)
        else:
            raise ValueError(f"File with this id ({self.id}) does not exist")

    def get_json(self):
        return self.file

    def download(self, path=f"C:\\Users\\{getpass.getuser()}\\Downloads\\"):
        with open(path + self.name, 'wb') as f:
            f.write((requests.get(self.url_file + "?raw")).content)
        return True

    def delete(self):
        self.r_delete = requests.get("https://api.uploadgram.me/delete/" + self.key,
                                     headers={"user-agent": USER_AGENT})
        return self.r_delete

    def rename(self, new_name: str):
        self.r_rename = requests.post("https://api.uploadgram.me/rename/" + self.key,
                                      data={"new_filename": new_name,
                                            "user-agent": USER_AGENT})
        return self.r_rename


class NewFile:
    def __init__(self, path):
        self.path = path
        self.url_upload = 'https://api.uploadgram.me/upload'
        self.file = open(self.path, "rb")

        self.key = ""
        self.id = ""
        self.url = ""
        self.url_import = ""

    def upload(self):
        """return {'ok': True, 'url': 'https://dl.uploadgram.me/new_file_id', 'delete': 'delete_key'}"""
        self.r = requests.post(self.url_upload,
                               headers={"user-agent": USER_AGENT},
                               files={"file_upload": self.file})
        self.key = self.r.json()["delete"]
        self.id = self.r.json()["url"].split("/")[-1]
        self.url = self.r.json()["url"]
        dict_part_url_to_import = ({str(self.key): {'filename': os.path.basename(self.path),
                                                       'size': int(
                                                           UploadgramFile(self.id, self.r.json()['delete']).file["size"]),
                                                       'url': str(self.url)}})
        self.url_import = "https://uploadgram.me/upload/#import:" + json.dumps(dict_part_url_to_import)
        return self.r.json()
