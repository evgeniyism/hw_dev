import requests
import yadisk
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': to_lang.lower(),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически
# определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    print(translate_it('привет', 'en'))

def start():
    choose_file = input('Введите адрес файла: ')
    choose_lang = input('Выберите язык: ')
    try:
        translate_and_save(choose_file, choose_lang)
        print(f'Сохранен файл с переводом translated_{choose_file}')
    except:
        print('Попытка не удалась, попробуйте еще раз')
        start()

def translate_and_save(file_path, to_lang):
    with open(file_path, 'r', encoding='UTF-8') as file:
        text = file.readlines()
        translated_text = translate_it(text,to_lang)
        result = open(f'translated_{file_path}', 'w')
        result.write(translated_text)
        result.close()
        try:
            upload_to_yandex(f'translated_{file_path}', f'/translated_{file_path}')
            return True
        except:
            print('Загрузка на Yandex.Disk не удалась')
            return False

def upload_to_yandex(file_to_upload, destination):
    user_disk = yadisk.YaDisk(token='OAuth AgAAAAANQ9ovAADLW7TaK7HlzkaYmDTRVICqxEQ')
    user_disk.upload(file_to_upload, destination)
    print(f'Файл {file_to_upload} успешно загружен на ваш Yandex.Диск')

start()

