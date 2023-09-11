# UploadgramPyAPI
![Alt](https://sun9-33.userapi.com/impg/uRrtaPGWd5M3u529Cr-PVUNORq-O4EwDjgwZyA/ak0CZq-ijFk.jpg?size=113x113&quality=96&sign=ce6642140fc672643d33e934d1235f7d&type=album "icon")

> Developing this project has been stopped because [uploadgram.me](https://uploadgram.me) was closed

This API can upload, download, remove and rename any files from the service [uploadgram.me](https://uploadgram.me) - a simple and fast file uploader that uses Telegram network as file storage.

__If you download this module, you confirm your agreement with the [Terms of Service](https://uploadgram.me/terms.html) and [DMCA Policy](https://uploadgram.me/dmca.html) of [Uploadgram.me](https://uploadgram.me/)__


[![Downloads](https://pepy.tech/badge/uploadgrampyapi)](https://pepy.tech/project/uploadgrampyapi)
[![Downloads](https://pepy.tech/badge/uploadgrampyapi/month)](https://pepy.tech/project/uploadgrampyapi)
[![Downloads](https://pepy.tech/badge/uploadgrampyapi/week)](https://pepy.tech/project/uploadgrampyapi)
[![Supported Versions](https://img.shields.io/pypi/pyversions/uploadgrampyapi.svg)](https://pypi.org/project/uploadgrampyapi)
[![PyPI](https://img.shields.io/pypi/v/uploadgrampyapi.svg)](https://pypi.org/project/uploadgrampyapi/)
[![PyPi](https://img.shields.io/pypi/format/uploadgrampyapi)](https://pypi.org/project/uploadgrampyapi/)
![GitHub top language](https://img.shields.io/github/languages/top/tankalxat34/UploadgramPyAPI)
[![GitHub last commit](https://img.shields.io/github/last-commit/tankalxat34/uploadgrampyapi)](https://github.com/tankalxat34/UploadgramPyAPI/commits/main)
[![GitHub Release Date](https://img.shields.io/github/release-date/tankalxat34/UploadgramPyAPI)](https://github.com/tankalxat34/UploadgramPyAPI/releases)

[![releases note](https://img.shields.io/badge/-releases%20note-black?style=for-the-badge&logo=markdown)](https://github.com/tankalxat34/UploadgramPyAPI/blob/main/releases_note.md)
[![github](https://img.shields.io/badge/-git%20hub-black?style=for-the-badge&logo=github)](https://github.com/tankalxat34/UploadgramPyAPI)
[![PyPi](https://img.shields.io/badge/-pypi-006DAD?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/UploadgramPyAPI)

[![GitHub Repo stars](https://img.shields.io/github/stars/tankalxat34/UploadgramPyAPI?style=social)](https://github.com/tankalxat34/UploadgramPyAPI)

**Author: [tankalxat34](mailto:tankalxat34@gmail.com?subject=User%20of%20UploadgramPyAPI)**

# Install
In your CMD perform this command:

```bat
pip install UploadgramPyAPI
```

# Quickstart
## Upload any file
```py
import UploadgramPyAPI
up_file = UploadgramPyAPI.NewFile("D:\\image.jpg")
up_file.upload()
```

## Delete any file
```py
import UploadgramPyAPI
up_file = UploadgramPyAPI.File("611e5e6237f6fg", "e3da26e9dddd2e01b8c0831370695e9088a96ff81e262fc2g")
up_file.delete()
```

## Rename any file
```py
import UploadgramPyAPI
up_file = UploadgramPyAPI.File("611e5e6237f6fg", "e3da26e9dddd2e01b8c0831370695e9088a96ff81e262fc2g")
up_file.rename("ItsNewNameForFile.jpg")
```

## Download any file
```py
import UploadgramPyAPI
up_file = UploadgramPyAPI.File("611e5e6237f6fg", "e3da26e9dddd2e01b8c0831370695e9088a96ff81e262fc2g")
up_file.download()
```

# Using
Now we can looking, how to use UploadgramPyAPI

## Upload new file

### Step 1
Firstly, you need to import the library:

```py
import UploadgramPyAPI
```

### Step 2
Next if you want to upload new file on uploadgram.me you need write this in your file:

```py
up_file = UploadgramPyAPI.NewFile("D:\\image.jpg")
```

This string will preparing your file to upload.

### Step 3
Write this line after the previous one.

```py
up_file.upload()
```

Now file `image.jpg` was uploaded in uploadgram.me and you was get the dictionary like here
```json
{
    "ok": "true", 
    "url": "https://dl.uploadgram.me/611e5e6237f6fg", 
    "delete": "e3da26e9dddd2e01b8c0831370695e9088a96ff81e262fc2g"
}
```

UploadgramPyAPI can parse this json-responce and create new attributes: `url`, `key` and `url_import`. 


## Important thing
_______
___Attribute `key` is a very important string for renaming and removing the file. You need to save its, else you won't do it.___
_______





Attribute `url_import` it's a simple url for import your file in a dashboard in https://dl.uploadgram.me.
Its look like this:

```json
https://uploadgram.me/upload/#import:{"e3da26e9dddd2e01b8c0831370695e9088a96ff81e262fc2g": {"filename": "image.jpg", "size": 55604, "url": "https://dl.uploadgram.me/611e5e6237f6fg"}}
```

Open this url in your browser and uploaded file will appear on the website! You can see something like this:

![Alt](https://sun9-54.userapi.com/impg/jppDL_T9_2FsDnc8pFLWdpqSzd91heDnbd8C4g/GJLh13On_aY.jpg?size=872x665&quality=96&sign=e32ba8f5877883060558882a1dd82345&type=album "slide")

So your code can be looking like this:
```py
import UploadgramPyAPI
up_file = UploadgramPyAPI.NewFile("D:\\image.jpg")
up_file.upload()
```

## Delete file

Also you can delete the file. Look!

### Step 1

If you have the `key` attribute for the file, you can delete its!

Firstly, you need to write this strings for connect to server and file on it:

```py
import UploadgramPyAPI
up_file = UploadgramPyAPI.File("611e5e6237f6fg", "e3da26e9dddd2e01b8c0831370695e9088a96ff81e262fc2g")
up_file.delete()
```

Last string deleted the `image.jpg` from `uploadgram.me`. If you want to make sure, you can open `url` in your browser. You will get the 404-error:

![Alt](https://sun9-78.userapi.com/impg/jKe2pjbifNJ7QNR3wvkiVWV7wzHebukEwd4Xlw/HbreA_TjlIg.jpg?size=922x665&quality=96&sign=b37ab6325819b5589ee8bbed9af61252&type=album "slide")

## Rename file

UploadgramPyAPI can rename the file.

We need use the `key` attribute for rename the file. 

The beginning is the same as in the previous steps:

```py
import UploadgramPyAPI
up_file = UploadgramPyAPI.File("611e5e6237f6fg", "e3da26e9dddd2e01b8c0831370695e9088a96ff81e262fc2g")

# this string will rename the filename
up_file.rename("ItsNewNameForFile.jpg")
```

And now you can see this situation:

![Alt](https://sun9-80.userapi.com/impg/LQagHS9h8wcDdqMtDBCMeyUlU5QZ_PKJ2Fd3jA/QFax68p4K_0.jpg?size=872x665&quality=96&sign=fcd29c8114e651fbcae85d17293442e4&type=album "slide")

## Download file

You can download the file from server:

```py
import UploadgramPyAPI
up_file = UploadgramPyAPI.File("611e5e6237f6fg", "e3da26e9dddd2e01b8c0831370695e9088a96ff81e262fc2g")

# this string will help download the file in the default download's folder
up_file.download()
```

File will appear in the download's folder:

![Alt](https://sun9-81.userapi.com/impg/2wvdZzEwgWKff9lzn2OIO1pXkG7yihLCMZxeyw/7Tzl3y78LJo.jpg?size=1021x850&quality=96&sign=6c43d00ea579a07566ba506b8032fa0e&type=album "slide")

Also you can write path to save file:

```py
up_file.download("D:\\MyMainFolder\\")
```

It's enough! Successful use of the UploadgramPyAPI library!
