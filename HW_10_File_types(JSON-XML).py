import json
import xml.etree.ElementTree as ET

# Работа с JSON
def json_filter(file_path):
    all_words = []
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
        sort = data['rss']['channel']['items']
        for i in sort:
            string_to_sort =  i['description'].split()
            string_to_sort = cleaning(string_to_sort)
            for word in string_to_sort:
                if len(word) > 6:
                    all_words.append(word)
    return all_words

# Работа с XML
def text_parser(file_path):
    parser = ET.XMLParser(encoding = 'utf-8')
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    info = tree.findall('channel/item/description')
    return info

def xml_filter(to_sort):
    all_words = []
    for i in to_sort:
        string_to_sort = i.text.split()
        string_to_sort = cleaning(string_to_sort)
        for word in string_to_sort:
            if len(word) > 6:
                all_words.append(word)
    return all_words

#Общие методы

#Фильтрация
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
    #Cчитаем кол-во слов, добавляем их в словарь
    res = {}
    for word in to_sort:
        if word in res.keys():
            res[word] += 1
        else:
            res[word] = 1
    # Выбираем 10
    final_dict = {}
    counter = 0
    for word in res.items():
        if word[1] in reversed(sorted(res.values())[-10:]) and counter != 10: # Проверяем значение на вхождение вы выборку "самые высокие значения, 10 последних"
            final_dict.update({word})
            counter +=1
    return (final_dict)

def print_top10(final_dict):
    top10 = list(final_dict.items())
    top10.sort(key=lambda i: i[1])
    for i in reversed(top10):
            print(i[0], ':', i[1])

def json_result(file_path):
    print('ТОП слов для JSON')
    print_top10(word_sorting(json_filter(file_path)))
    print('\n')


def xml_result(file_path):
    print('ТОП слов для XML')
    print_top10(word_sorting(xml_filter(text_parser(file_path))))
    print('\n')

json_result('newsafr.json')
xml_result('newsafr.xml')