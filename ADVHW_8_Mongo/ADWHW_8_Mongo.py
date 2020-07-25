from pymongo import MongoClient
import pymongo
import csv
from datetime import datetime
import re

class Mongo:

    def __init__(self,basename, **kwargs):
        self.client = MongoClient(**kwargs)
        self.active_db = self.client[basename]

    def read_data(self, csv_file):
        strings_to_add = []
        with open(csv_file, encoding='utf8') as csvfile:
            reader = csv.DictReader(csvfile)
            for concert in reader:
                price = int(concert['Цена'])
                concert['Цена'] = price
                date = datetime.strptime(concert['Дата'], '%d.%m').strftime('%d-%m-2020')
                date = datetime.strptime(date, '%d-%m-%Y')
                concert['Дата'] = date
                strings_to_add.append(concert)
        return strings_to_add

    def add_to_base(self, list_of_dicts, collection_to_add):
        result = collection_to_add.insert_many(list_of_dicts)
        print(result.inserted_ids)
        return True

    def show_collection(self, collection):
        result = (self.active_db[collection].find())
        for i in result:
            print(i)
        return result

    def find_cheapest(self, collection):
        result = self.active_db[collection].find().sort('Цена', pymongo.ASCENDING)
        return result

    def find_by_name(self, name, collection):
        search = f'(?i){name}'
        pattern = re.compile(search)
        result = self.active_db[collection].find({'Исполнитель':pattern}).sort('Цена', pymongo.ASCENDING)
        return result

    def test(self):
        base = Mongo('bogdanov')
        collection = base.active_db['concerts']
        # base.add_to_base(base.read_data('artists.csv'), collection)
        print('---В БАЗЕ---')
        base.show_collection('concerts')
        print('---СОРТИРОВКА ПО ЦЕНЕ---')
        for i in base.find_cheapest('concerts'):
            print(i)
        print('---ПОИСК ПО ИМЕНИ---')
        for  i in base.find_by_name('seconds to', 'concerts'):
            print(i)

base = Mongo('bogdanov')
collection = base.active_db['concerts']
base.test()