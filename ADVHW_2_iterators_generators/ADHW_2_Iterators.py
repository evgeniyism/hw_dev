import json
import wikipedia
import Advanced.ADVHW_2_iterators_generators.link_hasher as hash


class CountryIterator:

    def __init__(self, file, output_file):
        self.file = file
        self.output_file = output_file
        self.current = 0
        with open(file, 'r') as raw_data:
            self.country_list = json.load(raw_data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.country_list):
            raise StopIteration
        self.start = self.country_list[self.current]['name']['common']
        self.current += 1
        return self.start

    def request_country_url(self):
        self.wiki_urls = {}
        with open(self.output_file, 'a') as urls:
            counter = 1
            for country in CountryIterator(self.file, self.output_file):
                print(f'Requesting {counter}/{len(self.country_list)}')
                try:
                    counter += 1
                    country_page = wikipedia.page(country)
                    country_url = country_page.url
                    self.wiki_urls.update({country: country_url})
                except:
                    try:
                        find_country = wikipedia.suggest(country)
                        match_country = wikipedia.page(find_country)
                        country_url = match_country.url
                        self.wiki_urls.update({match_country: country_url})
                    except:
                        self.wiki_urls.update({country: 'Link not found'})
                        continue
        print(self.wiki_urls)
        return (self.wiki_urls)

    def urls_write_txt(self):
        data = CountryIterator(self.file, self.output_file).request_country_url()
        with open(self.output_file, 'w') as output:
            output.write(str(data))

    def urls_write_json(self):
        data = CountryIterator(self.file, self.output_file).request_country_url()
        with open(self.output_file, 'w') as output:
            output.write(json.dumps(data))


CountryIterator('countries.json', 'wiki.json').urls_write_json()
print(hash.LinkHasher('wiki.json').country_hashing())
