from vk_api import vk_api
import requests
from datetime import datetime
from Advanced.Finals_Advanced.constants import SLEEP
import json
import os.path


class VKinder:

    def __init__(self):
        # login = input('Введите номер телефона:')
        self.login = login
        # password = input('Введите пароль:')
        self.session = vk_api.VkApi(login, password, auth_handler=self.auth_handler)
        self.session.auth()
        self.token = self.session.token['access_token']
        self.user = self.session.token['user_id']

    def get_user(self):
        return self.user

    def auth_handler(self):
        """ Двухфакторная аутентификация.
        запрашивает код, отправляет на подтверждение
        """
        key = input("Введите код проверки: ")
        remember_device = True
        return key, remember_device

    def make_url(self, method):
        '''
        :param method: метод АПИ ВК
        :return: возвращает строку со ссылкой на метод
        '''
        default_url = 'https://api.vk.com/method/'
        url = default_url + method
        return url

    def get_params(self, params_to_add=None):
        '''
        Метод формирует словарь параметров запроса по умолчанию. Необязательный параметр
        позволяет добавить параметры или перезаписать
        :param params_to_add: параметры в виде словаря вида {'param': value}
        :return: словарь с параметрами запроса
        '''
        params = \
            {
                'access_token': self.token,
                'user_id': self.user,
                'v': '5.107'
            }
        if params_to_add:
            params.update(params_to_add)
        return params

    def make_request(self, method, params_to_add=None):
        '''
        Принимает метод, делает запрос к апи, возвращает сырой ответ
        :param method: метод АПИ ВК
        :param params_to_add: необязательно. Допольнительные параметры запроса
        :return: ответ метода ВК
        '''
        url = self.make_url(method)
        params = self.get_params(params_to_add)
        response = requests.get(url, params)
        SLEEP()
        if response.status_code == 200:
            return response
        else:
            raise Exception

    def get_city(self):
        search_request = input('Ваш город не указан в профиле, введите город: ')
        search = self.make_request('database.getCities',
                                     {'country_id': 1, 'q': search_request, 'count': 1})
        result = search.json()['response']['items'][0]
        return result

    def get_current_user_info(self):
        """
        Выполняет запрос к АПИ ВК
        Собирает информацию о пользователе в словарь
        :return: dict
        """
        data = self.make_request('users.get', {'fields': 'city, bdate, photo_50, sex, relation'})
        name = data.json()['response'][0]['first_name'] + ' ' + data.json()['response'][0]['last_name']
        age = data.json()['response'][0]['bdate']
        age = datetime.strptime(age, '%d.%m.%Y')
        age = (datetime.now() - age) // 365
        age = int(str(age)[0:3].strip())  # Здесь объект timedelta, который возвращает дни и часы. Можно преобразовывать
        # через доп функцию, но по-моему проще взять дни, поделить на 365 и привести к int. В итоге все равно получим
        # int значение для дальнейшей работы

        try:
            city = data.json()['response'][0]['city']['title']
            city_id = data.json()['response'][0]['city']['id']
        except:
            find_city = self.get_city()
            city = find_city['title']
            city_id = find_city['id']

        if data.json()['response'][0]['sex'] == 0:
            options = {'м': 1, 'ж': 2}
            choose_sex = input('Выберите ваш пол. М/Ж?:').lower()
            while choose_sex not in options.keys():
                choose_sex = input('Выберите ваш пол. М/Ж?:').lower()
            sex = options[choose_sex]
        else:
            sex = data.json()['response'][0]['sex']

        current_relationship_status = data.json()['response'][0]['relation']
        current_user = {'name': name, 'age': age, 'city': city, 'city_id': city_id, 'sex': sex,
                        'rel_status': current_relationship_status}
        return current_user

    def search(self):
        '''
        Выполняет запрос к АПИ ВК
        Собирает информацию о пользователях, подходящих по параметрам
        :return: json
        '''
        user = self.get_current_user_info()
        choice = [2 if user['sex'] == 1 else 1]
        search = self.make_request('users.search',
                                   {'fields': 'photo, screen_name, domain', 'city_id': user['city_id'], 'sex': choice,
                                    'status': 6, 'age_from': user['age'],
                                    'age_to': user['age'], 'count': 1000, 'offset': 0})
        result = search.json()
        return result

    def save_search_results(self, search_result):
        '''
        Принимает на вход сырой результат поиска, подготавливает к сбору фотографий
        :param search_result: результат метода search()
        :return: dict c имененм и ссылкой на профиль пользователя
        '''
        file_check = os.path.isfile('search_result.json')
        if file_check:
            with open('search_result.json', 'r', encoding='utf-8') as file:
                final_dict = json.load(file)
        else:
            final_dict = {}

        res = search_result['response']['items']
        for i in res:
            link = i['domain']
            to_add = {'vkid':str(i['id']), str(i['id']): {'name': i['first_name'] + ' ' + i['last_name'], 'link': 'http://vk.com/' + link}}
            final_dict.update(to_add)
        with open('search_result.json', 'w', encoding='utf-8') as file:
            json.dump(final_dict, file)
        return final_dict

    def top_3_photos(self, owner_id):
        '''
        Делает запрос к АПИ ВК
        Выбирает три топовых фото
        :param owner_id: id пользователя
        :return: list список со ссылками на фотографии
        '''
        photos = self.make_request('photos.get',
                                   {'owner_id': owner_id, 'album_id': 'profile', 'extended': 1, 'count': 1000})
        photos_list = photos.json()['response']['items']
        top_3_photos = []
        sorting = []
        for photo in photos_list:
            likes = photo['likes']['count']
            sorting.append(likes)
        sorting = sorted(sorting, reverse=True)[0:3]
        for photo in photos_list:
            if photo['likes']['count'] in sorting:
                top_3_photos.append(photo['sizes'][-1]['url'])
        while len(top_3_photos) > 3:
            top_3_photos.pop()
        return top_3_photos

    def show_10(self, search_results, page=0):
        '''
        возвращает 10 результатов для вывода
        :param search_results: результат метода save_search_results()
        :param page: страница для показа пользователя
        :return: dict
        '''
        matches = [k for k in search_results.keys()][page:page + 10]
        for match in matches:
            try:
                links = self.top_3_photos(match)
                if len(links) == 0:
                    links = 'Фото недоступно, добавьте пользователя в друзья'
            except:
                links = 'Профиль закрыт, добавьте пользователя в друзья'
            search_results[match].update({'photos': links})
            search_results[match].update({'page': page // 10})
            search_results[match].update({'vkid': match})
        base_slice_raw = {key: value for key, value in search_results.items() if key in matches}
        base_slice = [{key: value} for key, value in base_slice_raw.items()]
        return base_slice

