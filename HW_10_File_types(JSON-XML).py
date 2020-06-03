import json
import xml.etree.ElementTree as ET
from collections import Counter

# Работа с JSON
def json_filter(file_path):
    to_len_check = []
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
        sort = data['rss']['channel']['items']
        for i in sort:
            string_to_sort =  i['description'].split()
            string_to_sort = cleaning(string_to_sort)
            to_len_check.append(string_to_sort)
    return to_len_check

# Работа с XML
def xml_filter(file_path):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    info = tree.findall('channel/item/description')
    to_len_check = []
    for i in info:
        string_to_sort = i.text.split()
        string_to_sort = cleaning(string_to_sort)
        to_len_check.append(string_to_sort)
    return to_len_check

#Фильтрация
def len_check(list_to_sort):
    all_words = []
    for one_list in list_to_sort:
        for word in one_list:
            if len(word) > 6:
                all_words.append(word)
    return all_words

def cleaning(text_to_clean):
    filtered_list = []
    for i in text_to_clean:
        result_string = i.lower()
        to_del = '!@#$%^&*()_+<>?:|{},./;"'
        to_replace = '                        '
        replace_tab = str.maketrans(to_del,to_replace)
        result_string = result_string.translate(replace_tab).strip()
        if result_string.isalpha():
            filtered_list.append(result_string)
        else:
            continue
    return filtered_list

def word_sorting(to_sort):
    res = {}
    for word in to_sort:
        if word in res.keys():
            res[word] += 1
        else:
            res[word] = 1
    choose_top_n = Counter(res)
    final_dict = choose_top_n.most_common(10)
    return final_dict

def print_top10(final_dict):
    for i in final_dict:
            print(i[0], ':', i[1])

def json_result(file_path):
    print('ТОП слов для JSON')
    print_top10(word_sorting(len_check(json_filter(file_path))))
    print('\n')


def xml_result(file_path):
    print('ТОП слов для XML')
    print_top10(word_sorting(len_check(xml_filter(file_path))))
    print('\n')

json_result('newsafr.json')
xml_result('newsafr.xml')