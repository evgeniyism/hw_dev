import requests
from time import sleep
import json

def get_user_groups(USER_ID):
    '''
    Запрашивaет список групп, в которых состоит юзер
    :param USER_ID: id юзера
    :return: list со списком групп
    '''
    URL = f'https://api.vk.com/method/groups.get?user_id={USER_ID}'
    params = \
            {
                'access_token': API_TOKEN,
                'user_id': USER_ID,
                'v': '5.107'
            }
    try:
        response = requests.get(URL, params)
        print(f' > идет запрос к списку групп {USER_ID}')
        user_groups_list = response.json()['response']['items']
        print(f' + запрос успешен')
        return(user_groups_list)
    except:
        print(f' - Запрос к пользователю {USER_ID} не удался')
        print(response.json()['error']['error_msg'])

def get_friends_list(USER_ID):
    '''
    Запрашивает список id друзей пользователя.
    :param USER_ID: id юзера
    :return: list со списком друзей
    '''
    URL = f'https://api.vk.com/method/friends.get?user_id={USER_ID}'
    params = \
            {
                'access_token': API_TOKEN,
                'user_id': USER_ID,
                'v': 5.107
            }

    response = requests.get(URL, params)
    print(f' > идет запрос к списку друзей {USER_ID}')
    friends_list = response.json()['response']['items']
    return(friends_list)

def all_friends_groups_set(friends_list):
    '''
    Запрашивает список групп, в которых состоят друзья пользователя
    Собирает уникальные значения
    :param friends_list: список друзей
    :return: set
    '''
    all_groups = []
    timer = len(friends_list)+1
    timer_count = 1
    for friend in friends_list:
        print(f'Запрос {timer_count}/{timer}')
        timer_count += 1
        one_user_groups = get_user_groups(friend)
        sleep(0.34)
        if one_user_groups == None:
            continue
        all_groups.extend(one_user_groups)
    all_groups_unique = set(all_groups)
    return(all_groups_unique)


def format_res_to_json(unique_groups_of_user):
    '''
    Получает на вход список id уникальных групп
    Запрашивает информацию о группах
    Формирует json
    :param unique_groups_of_user: список id груп
    :return: json
    '''
    unique_groups_of_user = list(unique_groups_of_user)
    group_string = ','.join(str(x) for x in unique_groups_of_user)

    URL = f'https://api.vk.com/method/groups.getById?'
    params = \
        {
            'access_token': API_TOKEN,
            'group_ids': group_string,
            'fields': 'members_count',
            'v': 5.107
        }

    response = requests.get(URL, params)
    groups_info = response.json()['response']
    final_dict = []

    for i in groups_info:
        try:
            final_dict.append({'name': i['name'], 'gid': i['id'], 'members_count': i['members_count']})
        except:
            print(f' - Запрос к группе', i['name'], 'не удался')
            print(response.json()['error']['error_msg'])
    result = json.dumps(final_dict, ensure_ascii=False)
    return (result)

def start(USER_ID, API_TOKEN):
    '''
    Вычитает из множества групп юзера множество групп друзей
    :param USER_ID:
    :param API_TOKEN:
    :return: возвращает итоговый json
    '''
    one_user_groups = set(get_user_groups(USER_ID))
    users_friends_groups = all_friends_groups_set(get_friends_list(USER_ID))
    unique_groups_of_user = one_user_groups - users_friends_groups
    final_result = format_res_to_json(unique_groups_of_user)
    print(final_result)
    return final_result

if __name__ == '__main__':
    USER_ID = '171691064'
    API_TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    start(USER_ID, API_TOKEN)