from pymongo import MongoClient
import csv
from datetime import datetime

class Mongo:

    def __init__(self,basename, **kwargs):
        self.basename = basename
        self.client = MongoClient(**kwargs)
        self.active_db = self.client[basename]

    def new_collection(self, collection_name):
        collection = self.active_db[collection_name]
        return collection

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
        # print(result.inserted_ids)
        return True

    def show_collection(self, collection):
        result = (self.active_db[collection].find())
        for i in result:
            print(i)
        return result

    # def find_by_name(self, user_id, collection):
    #     search = f'{id}'
    #     pattern = re.compile(search)
    #     result = self.active_db[collection].find({'Исполнитель':pattern}).sort('Цена', pymongo.ASCENDING)
    #     return result
