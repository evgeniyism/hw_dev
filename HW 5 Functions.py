documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;

def showpeople():
    document_number = input('Введите номер документа: ')
    for person in documents:
        if person['number'] == document_number:
            return(person['name'])
    return ('Документ с таким номером не найден')

# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.

def find_shelf():
    document_number = input('Введите номер документа: ')
    for key, value in directories.items():
        if document_number in value:
            return('Документ на полке ' + key)
    return('Документ с таким номером не найден')

# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";

def print_documents_list():
    documents_list = []
    for doc in documents:
         documents_list.append(str(doc['type'] + ' "' + doc['number'] + '" ' + '"' + doc['name'] +'"'))
    return('\n'.join(documents_list))

# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца
# и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться
# добавить документ на несуществующую полку.
def add_new_document():
    shelf_check = False
    doc_type = input('Введите тип документа: ')
    doc_number = input('Введите номер документа: ')
    name = input('Введите имя владельца: ')
    whatshelf = input('Введите номер полки для хранения: ')
    if shelf_check == False:
        while whatshelf.isdigit() == False:
            print('НЕ УДАЛОСЬ: введите номер полки в виде числа.')
            whatshelf = input()
        else:
            shelf_check = True
    newitem = {}
    newitem.update({'type': doc_type})
    newitem.update({'number': doc_number})
    newitem.update({'name': name})
    documents.append(newitem)
    document_to_place = newitem['number']
    directories[whatshelf].append(document_to_place)
    print(f' Документ: {doc_type}, номер {doc_number}, на имя {name} успешно добавлен. Хранится на полке номер {whatshelf}.')
    print(directories)
    print(documents)

def delete_document():
    req = input('Введите номер документа: ')
    req = req.replace(' ', '')
    req = req.replace('-', '')
    req = req.replace('/', '')
    req = req.replace('_', '')
    req = req.replace('|', '')
    checkA = False

    if checkA == False:
        for i in documents:
            x = i['number']
            x = x.replace(' ', '')
            x = x.replace(' ', '')
            x = x.replace('-', '')
            x = x.replace('/', '')
            x = x.replace('_', '')
            x = x.replace('|', '')
            if req in x:
                documents.remove(i)
                i.pop('name')
                print('Документ успешно удален.')
                checkA = True
            else:
                checkA = False

    checkB = False
    if checkB == False:
        for shelf in directories.keys():
            for i in directories.values():
                for x in i:
                    x = x.replace(' ', '')
                    x = x.replace(' ', '')
                    x = x.replace('-', '')
                    x = x.replace('/', '')
                    x = x.replace('_', '')
                    x = x.replace('|', '')
                    if req == x:
                        i.remove(x)

    if checkA == False and checkB == False:
        print('Номер документа не найден')

def move_doc_to_shelf():
    req = input('Введите номер документа: ')
    moveto = input('Введите новую полку для документа: ')
    req = req.replace(' ', '')
    req = req.replace('-', '')
    req = req.replace('/', '')
    req = req.replace('_', '')
    req = req.replace('|', '')
    check = False
    for shelf in directories.keys():
        for i in directories.values():
            for x in i:
                unformatted = x
                x = x.replace(' ', '')
                x = x.replace(' ', '')
                x = x.replace('-', '')
                x = x.replace('/', '')
                x = x.replace('_', '')
                x = x.replace('|', '')
                if req == x:
                    if moveto in directories.keys():
                        check = True
                        directories.update({moveto: [unformatted]})
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

def main():
    user_input = input('Введите команду: ')
    commands = ['p', 'people', 's', 'shelf', 'l', 'list', 'ads', 'add shelf', 'd', 'delete', 'm', 'move', 'a', 'add', 'help', 'stop']
    go = True
    while go == True:
        if user_input in commands:
                if user_input == 'p' or user_input == 'people':
                    print('запускаю People')
                    print(showpeople())
                    user_input = input('Введите команду: ')
                elif user_input == 's' or user_input == 'shelf':
                    print('запускаю Shelf')
                    print(find_shelf())
                    user_input = input('Введите команду: ')
                elif user_input == 'l' or user_input == 'list':
                    print('запускаю List')
                    print(print_documents_list())
                    user_input = input('Введите команду: ')
                elif user_input == 'ads' or user_input == 'add shelf':
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

main()