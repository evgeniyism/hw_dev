from Advanced.Finals_Advanced.VKinder_methods import VKinder
from Advanced.Finals_Advanced.mongo_handler import Mongo
from pprint import pprint
import json
from Advanced.Finals_Advanced.constants import *
from copy import deepcopy



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
        while self.check_matches_in_base(clear_matches_to_base) == True:
            self.page +=10
            clear_matches_to_base = self.instance.show_10(self.full_list, page=self.page)
        pprint(clear_matches_to_base)
        copy_to_base = deepcopy(clear_matches_to_base)
        self.show_result_and_write_to_base(copy_to_base)
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
        copy_to_base = deepcopy(clear_matches_to_base)
        self.show_result_and_write_to_base(copy_to_base)
        return clear_matches_to_base

    # def send_list_to_base(self, list_to_base):
    #     self.show_result_and_write_to_base(copy_to_base)

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
        return None

    def save_result_to_file(self, info_to_save):
        '''
        Получает на вход список словарей, кодирует в json, пишет в файл
        :param info_to_save: list of dicts
        :return:
        '''
        filename = f'Search_{self.user}_page_{self.page//10}.json'
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(info_to_save, file)
        print(f'Файл {filename} успешно сохранен')
        return True

    def check_matches_in_base(self, search_list_of_dicts):
        to_check = search_list_of_dicts
        in_base = self.base.find_by_id_in_base(str(self.user))
        a = list(to_check[0].keys())
        if a[0] in in_base:
            return True
        else:
            return False

    def start(self):
        '''
        UI ;)
        :return:
        '''
        print('Идет поиск')
        quit_program = False
        result = self.search_first_page()
        while not quit_program:
            user_input = input(MENU_TEXT_MAIN)
            if user_input in ACCEPTABLE_ANSWERS:
                if user_input == '1':
                    self.save_result_to_file(result)
                if user_input == '2':
                    result = self.search_next_page()
                if user_input == 'quit':
                    break
            else:
                print('НЕВЕРНЫЙ ВВОД')
        print('Программа завершена')

