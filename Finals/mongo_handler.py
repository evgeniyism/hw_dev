from functools import reduce

from pymongo import MongoClient
import csv
from datetime import datetime
import re


class Mongo:

    def __init__(self, basename, **kwargs):
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
        return True

    def find_by_id_in_base(self, collection):
        cursor = self.active_db[collection].find({})
        vkids = set()
        for i in cursor:
            vkids.update(i.keys())
        try:
            vkids.remove('_id')
        except:
            pass
        return vkids
