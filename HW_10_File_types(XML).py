import xml.etree.ElementTree as ET

def text_parser(file_path):
    file_path = 'newsafr.xml'
    parser = ET.XMLParser(encoding = 'utf-8')
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    info = tree.findall('channel/item/description')
    return info

def xml_filter(to_sort):
    all_words = []
    for i in to_sort:
        string_to_sort = i.text.split()
        for word in string_to_sort:
            if len(word) > 6:
                all_words.append(word)
    return all_words

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

print_top10(word_sorting(xml_filter(text_parser('newsafr.xml'))))