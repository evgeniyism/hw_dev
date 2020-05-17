documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}

def cleartrash(inf):
    inf = inf.replace(' ', '')
    inf = inf.replace('-', '')
    inf = inf.replace('/', '')
    inf = inf.replace('_', '')
    inf = inf.replace('|', '')
    return(inf)

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def find_name_by_document():
    req = input('Введите номер документа: ') 
    req = cleartrash(req)
    check = False
    for i in documents:
        x = i['number']
        x = cleartrash(x)
        if req in x:
            print('Владелец документа: ', i['name'])
            check = True
            break
        else:
            check = False
    if check == False:
        print('Номер документа не найден')

# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится
# Правильно обработайте ситуацию, когда пользователь будет вводить несуществующий документ.

def find_shelf_by_doc():
    requested_shelf = ''
    req = input('Введите номер документа: ') 
    req = cleartrash(req)
    check = False
    for shelf in directories.keys():
        for i in directories.values():
            for x in i:
                x = cleartrash(x)
                if req == x:
                    check = True
                    requested_shelf = shelf
                    print('Документ на полке №', requested_shelf)
        break
    if check == False:
        print('Номер документа не найден')

# l – list – команда, которая выведет список всех документов в формате
# passport "2207 876234" "Василий Гупкин"  

def print_all_docs():
    for i in documents:
        print(i['type'], ' "', i['number'], '"', ' "', i['name'],'"', sep = '')

# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень

def new_shelf_add():
    exist = []
    for i in directories:
        i = str(i)
        exist.append(i)
    print('Существующие полки :', exist)
    newshelf = input('Ведите номер новой полки: ')
    if newshelf.isdigit() == True:   
        if newshelf in directories.keys():
            print('НЕ УДАЛОСЬ: такая полка уже существует')
        else:
            directories.update({newshelf: []})
            print('Полка №', newshelf, 'успешно добавлена.')
    else:
        print('НЕ УДАЛОСЬ: введите номер полки в виде числа.')

#- d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. 
# Предусмотрите сценарий, когда пользователь вводит несуществующий документ;  

def delete_document():
    req = input('Введите номер документа: ') 
    req = cleartrash(req)
    checkA = False

    if checkA == False:   
        for i in documents:
            x = i['number']
            t = x
            x = cleartrash(x)
            if req == x:
                documents.remove(i)
                i.pop('name')
                print('Документ номер' , t, 'успешно удален.')
                checkA = True
            else:
                checkA = False

    checkB = False
    if checkB == False:
        for shelf in directories.keys():
            for i in directories.values():
                for x in i:
                    t = x
                    x = cleartrash(x)
                    if req == x:
                        i.remove(t)

    if checkA == False and checkB == False:
        print('Номер документа не найден')

# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. 
# Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ 
# на несуществующую полку;

def move_doc_to_shelf():
    req = input('Введите номер документа: ') 
    moveto = input('Введите новую полку для документа: ') 
    req = cleartrash(req)
    check = False
    for shelf in directories.keys():
        for i in directories.values():
            for x in i:
                unformatted = x
                x = cleartrash(x)
                if req == x:
                    if moveto in directories.keys():
                        check = True
                        directories[moveto].append(unformatted)
                        i.remove(unformatted)
                    else:
                        print('Желаемая полка не найдена. Чтобы создать полку используйте команду "ads".')
                        check = True                        
                        break
        break
    if check == False:
        print('Номер документа не найден')
    if check == True:                       
        print('Документ успешно перемещен на полку ', moveto)

# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, 
# тип, имя владельца и номер полки, на котором он будет храниться.


def add_new_document():
    shelfcheking = False
    doc_type = input('Введите тип документа: ')
    doc_number = input('Введите номер документа: ')
    name = input('Введите имя владельца: ')
    whatshelf = input('Введите номер полки для хранения: ')
    if shelfcheking == False:
        while whatshelf.isdigit() == False:
            print('НЕ УДАЛОСЬ: введите номер полки в виде числа.')
            whatshelf = input()
#         while whatshelf in directories.keys():
#             print('Такая полка уже существует, введите другой номер.')
#             whatshelf = input()
        else:
            shelfchek = True
    newitem = {}
    newitem.update({'type': doc_type})
    newitem.update({'number': doc_number})
    newitem.update({'name': name})
    documents.append(newitem)
    f = [newitem['number']]
    directories[whatshelf].append(doc_number)

def sos():
    helpme = ['- p или people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит',
              '- s или shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится',
              '- l или list – команда, которая выведет список всех документов в формате',
              '- ads или add shelf – команда, которая спросит номер новой полки и добавит ее в перечень',
              '- d или delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок',
              '- m или move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую',
              '- a или add – команда, которая добавит новый документ в каталог и в перечень полок)',
              '- stop - останавливает программу'
    ]
    for i in helpme:
        print(i)

def main(): 
    user_input = input('Введите команду: ')
    commands = ['p', 'people', 's', 'shelf', 'l', 'list', 'ads', 'add shelf', 'd', 'delete', 'm', 'move', 'a', 'add', 'help', 'stop']
    go = True
    while go == True:
        if user_input in commands:
                if user_input == 'p' or user_input == 'people':
                    print('запускаю People')
                    find_name_by_document()
                    user_input = input('Введите команду: ')
                elif user_input == 's' or user_input == 'shelf':
                    print('запускаю Shelf')
                    find_shelf_by_doc()
                    user_input = input('Введите команду: ')
                elif user_input == 'l' or user_input == 'list':
                    print('запускаю List')
                    print_all_docs()
                    user_input = input('Введите команду: ')
                elif user_input == 'ads' or user_input == 'add shelf': #не смог реализовать 'as', как в условии, т.к. системное имя. Заменил на 'ads'
                    print('запускаю Add Shelf')
                    new_shelf_add()
                    user_input = input('Введите команду: ')
                elif user_input == 'd' or user_input == 'delete':
                    print('запускаю Delete')
                    delete_document()
                    user_input = input('Введите команду: ')
                elif user_input == 'm' or user_input == 'move':
                    print('запускаю Move')
                    move_doc_to_shelf()
                    user_input = input('Введите команду: ')
                elif user_input == 'a' or user_input == 'add':
                    print('запускаю Add')
                    add_new_document()
                    user_input = input('Введите команду: ')
                elif user_input == 'help':
                    print('запускаю Help')
                    sos()
                    user_input = input('Введите команду: ')
                elif user_input == 'stop':
                    print('Программа завершена')
                    go = False
        else:
            print('Неверная команда, попробуйте еще раз.')
            print('Для справки наберите help.')
            user_input = input('Введите команду: ')


# Необходимо реализовать пользовательские команды (внимание! это не название функций, которые должны быть выразительными, а команды, которые вводит пользователь, чтобы получить необходимый результат):
#   
# - p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;  
# - s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится  
# Правильно обработайте ситуацию, когда пользователь будет вводить несуществующий документ.
# - l – list – команда, которая выведет список всех документов в формате   
# **passport "2207 876234" "Василий Гупкин"**  
# - as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень
# - d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;  
# - m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;  
# - a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.

main()

print(documents)
print(directories)