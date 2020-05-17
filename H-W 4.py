# # Задание 1. Дан список с визитами по городам и странам. Напишите код, который возвращает
# # отфильтрованный список geo_logs, содержащий только визиты из России.
#
# geo_logs = [
#     {'visit1': ['Москва', 'Россия']},
#     {'visit2': ['Дели', 'Индия']},
#     {'visit3': ['Владимир', 'Россия']},
#     {'visit4': ['Лиссабон', 'Португалия']},
#     {'visit5': ['Париж', 'Франция']},
#     {'visit6': ['Лиссабон', 'Португалия']},
#     {'visit7': ['Тула', 'Россия']},
#     {'visit8': ['Тула', 'Россия']},
#     {'visit9': ['Курск', 'Россия']},
#     {'visit10': ['Архангельск', 'Россия']}]
# geo_logs_filtering = geo_logs.copy()
# for visit in geo_logs_filtering:
#     for value in visit.values():
#         if value[1] != 'Россия':
#             geo_logs.remove(visit)
# print (geo_logs)

# geo_logs = [
#     {'visit1': ['Москва', 'Россия']},
#     {'visit2': ['Дели', 'Индия']},
#     {'visit3': ['Владимир', 'Россия']},
#     {'visit4': ['Лиссабон', 'Португалия']},
#     {'visit5': ['Париж', 'Франция']},
#     {'visit6': ['Лиссабон', 'Португалия']},
#     {'visit7': ['Тула', 'Россия']},
#     {'visit8': ['Тула', 'Россия']},
#     {'visit9': ['Курск', 'Россия']},
#     {'visit10': ['Архангельск', 'Россия']}]
# geo_logs_filtered = []
# for visit in geo_logs:
#     if 'Россия' in [x for x in visit.values()][0][1]:
#         geo_logs_filtered.append(visit)
# print(geo_logs_filtered)




# # Задание 2. Выведите на экран все уникальные гео-ID из значений
# # словаря ids. Т. е. список вида [213, 15, 54, 119, 98, 35]
# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}
# result = []
# for key in ids:
#     result.extend(set(ids.get(key)))
# result = list(set(result))
# print(result)



# Задание 3. Дан список поисковых запросов. Получить распределение количества слов в них.
# Т. е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт',
# ]
# distribution = []
# for i in queries:
#     newkey = len((i.strip().split()))
#     distribution.append(newkey)
# res = dict.fromkeys(distribution, 0)
# for i in distribution:
#     if i in res.keys():
#         res[i]+=1
# for key in res.keys():
#     res[key] = round(((res.get(key))/len(distribution))*100)
# print(res)


# Задание 4. Дана статистика рекламных каналов по объемам продаж. Напишите скрипт,
# который возвращает название канала с максимальным объемом. Т. е. в данном примере скрипт должен возвращать 'yandex'.

# stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
# for key, value in stats.items():
#     if value == (max(stats.values())):
#         print(key)


# Задание 5. *(Необязательное) Напишите код для преобразования
# произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100]
# (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

# todict = ['2018-01-01', 'yandex', 'cpc', 100]
# newdict = {}
# counter = 0
# for i in todict:
#     if counter == 0:
#         newdict[todict[-2]] = todict[-1]
#         todict.pop()
#         counter +=1
#     else:
#         newdict[todict[-2]] = newdict
#         todict.pop()
# print(newdict)

# todict = ['2018-01-01', 'yandex', 'cpc', 100]
# newdict = {}
# final_dict = {}
# counter = 0
# stop = len(todict)
# for i in todict:
#     if counter == 0:
#         print(counter)
#         key = todict[stop-2]
#         value = todict[stop-1]
#         newdict = {key: value}
#         counter+=1
#     if counter < stop-1:
#         print(counter)
#         key = todict[stop-2-counter]
#         value = newdict
#         final_dict = {key: value}
#         newdict = final_dict
#         counter+=1
# print(final_dict).

todict = ['2018-01-01', 'yandex', 'cpc', 100]
newdict = {todict[-2]:todict[-1]}
del todict[-2:]
for i in reversed(todict):
    todict.pop()
    newdict = {i:newdict}
print(newdict)
