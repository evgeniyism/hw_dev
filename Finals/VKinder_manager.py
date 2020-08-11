from Advanced.Finals_Advanced.VKinder_methods import VKinder
from Advanced.Finals_Advanced.mongo_handler import Mongo
from pprint import pprint
import json
from Advanced.Finals_Advanced.constants import *



class VKinder_search:

    def __init__(self):
        self.instance = VKinder()
        self.user = self.instance.get_user()
        self.base = Mongo('VKinder')
        self.collection = self.base.new_collection(self.user)
        self.page = 0
        self.full_list = self.search_matches()

    def search_matches(self):
        '''
        Ищет варианты совпадений
        :return: dict
        '''
        results = self.instance.search()
        final_res = self.instance.save_search_results(results)
        return final_res

    def search_first_page(self):
        '''
        Возвращает топ 10 пользователей при первом поиске
        :return:
        '''
        clear_matches_to_base = self.instance.show_10(self.full_list, page=self.page)
        to_base = self.show_result_and_write_to_base(clear_matches_to_base)
        return clear_matches_to_base

    def search_next_page(self):
        '''
        Возвращает ТОП 10 при последующих поисках
        :return:
        '''
        if self.page < len(self.full_list) // 10:
            self.page += 10
        else:
            print('Вы достигли конца списка')
        clear_matches_to_base = self.instance.show_10(self.full_list, page=self.page)
        to_base = self.show_result_and_write_to_base(clear_matches_to_base)
        return clear_matches_to_base

    def show_result_and_write_to_base(self, result):
        '''
        Выводит результат, отправляет копию в базу
        :param result:
        :return:
        '''
        print(SEPARATOR)
        print('Результат поиска')
        pprint(result)
        written = self.base.add_to_base(result, self.collection)
        return written

    def save_result_to_file(self, info_to_save):
        '''
        Получает на вход список словарей, кодирует в json, пишет в файл
        :param info_to_save: list of dicts
        :return:
        '''
        filename = f'Search_{self.user}_page_{self.page}.json'
        info_to_save = str(info_to_save)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(info_to_save, file)
        print(f'Файл {filename} успешно сохранен')
        return True

    def start(self):
        '''
        UI ;)
        :return:
        '''
        print('Идет поиск')
        quit = False
        result = self.search_first_page()
        user_input = input(MENU_TEXT_MAIN)
        while not quit:
            if user_input in ACCEPTABLE_ANSWERS:
                if user_input == '1':
                    self.save_result_to_file(result)
                    user_input = input(MENU_TEXT_MAIN)
                if user_input == '2':
                    result = self.search_next_page()
                    user_input = input(MENU_TEXT_MAIN)
                if user_input == 'quit':
                    quit = True
            else:
                print('Я в повторе')
                user_input = input(MENU_TEXT_MAIN)
        print('Программа завершена')


