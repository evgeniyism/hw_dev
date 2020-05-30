import json

def json_filter(file_path):
    all_words = []
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
        sort = data['rss']['channel']['items']
        for i in sort:
            string_to_sort =  i['description'].split()
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

print_top10(word_sorting(json_filter('newsafr.json')))