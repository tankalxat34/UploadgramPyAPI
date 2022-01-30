# Version 1.6
## EN
**The main thing in 1.6:**

Added new class `UploadgramPyAPI.Random`, that can generate random `ID` or `KEY`. If you want to import any file **(you can import also someone else's file)** from Uploadgram in your [Dashboard]("https://uploadgram.me/upload/#/"), you need in parameter `KEY` in class `UploadgramPyAPI.File` write this random `KEY`. For example:
```py
import UploadgramPyAPI
import webbrowser

# here generating a random KEY
fake_key = UploadgramPyAPI.Random("key").get()

# connecting to file with using the generated key 
up_file = UploadgramPyAPI.File("614e0729b6279g", fake_key)

# this line are opening url_import in your browser and you can see this file in Dashboard
webbrowser.open_new_tab(up_file.url_import)
```

- Added new attribute `self.scanned` in class `File`. That is equal `True` if in file accepted absence any virus or any violations
- Now `self.url_import` will be equal `None`, if that unavailable generate
- Added new class `UploadgramPyAPI.Random`. Now you can generate a random `ID` or `KEY`
- Added new class `UploadgramPyAPI.ServiceRules` for getting the actual text of [Terms of Service](https://uploadgram.me/terms.html) and [DMCA Policy](https://uploadgram.me/dmca.html)
- Added new exception `UploadgramInvalidKey` that will be show if you are using incorrect `KEY` for file
- Added new exception `UploadgramInvalidValue` that will be show if you are using incorrect value for any parameter
- Corrected error that unsuccessful result of delete or rename the file was never showed in program
- Corrected grammar error in the name of variable `self.check_to_available` in class `UploadgramPyAPI.NewFile`
- Added links to [Terms of Service](https://uploadgram.me/terms.html), [DMCA Policy](https://uploadgram.me/dmca.html), [PyPi](https://pypi.org/project/uploadgrampyapi/), [PePy](https://pepy.tech/project/UploadgramPyAPI) and on [telegram's author](https://t.me/tankalxat34)
- Added `README.md` to [PyPi](https://pypi.org/project/uploadgrampyapi/)
- Now all information of new releases will be double in Russian

Update to 1.6:
```bat
pip install --upgrade UploadgramPyAPI
```

Download:
```bat
pip install UploadgramPyAPI
```

_______________________________
## RU

**Главное в 1.6:**

Добавлен класс `Random`, благодаря которому вы можете сгенерировать случайный `ID` или `KEY`. Причем, если вы хотите импортировать какой-либой файл **(в то числе и чужой)** из Uploadgram себе в [Dashboard]("https://uploadgram.me/upload/#/"), вам нужно в качестве параметра `KEY` класса `UploadgramPyAPI.File` указать этот случайный `KEY`. Пример:
```py
import UploadgramPyAPI
import webbrowser

# генерация случайного KEY
fake_key = UploadgramPyAPI.Random("key").get()

# подключение к файлу с использованием сгенерированного случайного ключа 
up_file = UploadgramPyAPI.File("614e0729b6279g", fake_key)

# этой строкой вы открываете url_import у себя в браузере и необходимый файл появится у вас в Dashboard
webbrowser.open_new_tab(up_file.url_import)
```

- Добавлен новый атрибут `scanned` класса `UploadgramPyAPI.File`. Он равен `True`, если в файле подтверждено отсутствие вирусов или каких-либо нарушений
- Теперь `url_import` будет становится равным `None`, если его невозможно сгенерировать
- Добавлен класс `UploadgramPyAPI.Random`, благодаря которому можно сгенерировать случайный `id` или `key`
- Добавлен класс `UploadgramPyAPI.ServiceRules` для получения актуального текста из [Terms of Service](https://uploadgram.me/terms.html) и [DMCA Policy](https://uploadgram.me/dmca.html)
- Добавлена ошибка `UploadgramInvalidKey`, которая возникает, если вы используете неподходящий или неправильный `key` для файла
- Добавлена ошибка `UploadgramInvalidValue`, которая возникает, если вы используете неправильное или неподходящее значение для какого либо параметра
- Исправлена ошибка, при которой неудачный результат удаления или переименования файла никак не отражался в ходе выполнения программы
- Исправлена ошибка в названии переменной `self.check_to_available`
- Добавлены ссылки на [Terms of Service](https://uploadgram.me/terms.html), [DMCA Policy](https://uploadgram.me/dmca.html), [PyPi](https://pypi.org/project/uploadgrampyapi/), [PePy](https://pepy.tech/project/UploadgramPyAPI) и на [Telegram автора](https://t.me/tankalxat34)
- Добавлено описание проекта на [PyPi](https://pypi.org/project/uploadgrampyapi/)
- Теперь информация об изменениях будет дублироваться и на русском языке

Обновить:
```bat
pip install --upgrade UploadgramPyAPI
```

Скачать:
```bat
pip install UploadgramPyAPI
```

# Version 1.5
## EN
- Simplified error classes.
- Added the `LENGTH_ID` constant.
- Now the `KEY` parameter has become optional. To delete or rename a file, it is enough to specify the `KEY` in the `ID` parameter.
- Now the `ID` and `URL` parameters are determined directly from the server response.
- The `URL_IMPORT` parameter no longer receives a link if the file `ID` is specified instead of the `KEY` parameter.
- The `UploadgramUsingKeyError` error now has an updated description.
- Now the `userTelegramId` and `userId` parameters can take the value None of the "None" type if they are not in the response from the server.
- The variable `self.json` has been renamed to the `self.readfile` of the `UploadgramPyAPI.NewFile` class.
- Minor edits have been made to `__doc__`.
- Other edits have been made to the code. 

Update to 1.5:
```bat
pip install --upgrade UploadgramPyAPI
```

Download:
```bat
pip install UploadgramPyAPI
```
## RU
- Упрощены классы ошибок.
- Добавлена константа `LENGTH_ID`.
- Теперь параметр `KEY` стал необязательным. Для удаления или переименования файла достаточно указать `KEY` в параметр `ID`.
- Теперь параметры `ID` и `URL` определяется напрямую от ответа сервера.
- Параметр `URL_IMPORT` больше не получает ссылку, если вместо параметра `KEY` указан `ID` файла.
- Ошибка `UploadgramUsingKeyError` теперь имеет обновленное описание.
- Теперь параметры `userTelegramId` и `userIp` могут принимать значение None типа "None", если в ответе от сервера их нет.
- Переименована переменная `self.json` на `self.readfile` класса `UploadgramPyAPI.NewFile`.
- Внесены незначительные правки в `__doc__`.
- Внесены другие правки в код.


Обновить:
```bat
pip install --upgrade UploadgramPyAPI
```

Скачать:
```bat
pip install UploadgramPyAPI
```
