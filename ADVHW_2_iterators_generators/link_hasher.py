from hashlib import md5
import json


class LinkHasher:

    def __init__(self, file_to_hash):
        self.file_to_hash = file_to_hash


    def country_hashing(self):
        with open(self.file_to_hash, 'r') as raw_file:
            self.file_to_hash = json.load(raw_file)
            hashed_links = {key: md5(value.encode()).hexdigest() for key, value in self.file_to_hash.items()}
            return hashed_links
