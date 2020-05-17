# Задача №1, №2

operation = input('Введите выражение в польской нотации через пробел:')
try:
    separate = operation.split(sep = ' ')
    function = separate[0]
    num1 = separate[1]
    num2 = separate[2]
except:
    print('Введите два числа')
    raise ValueError

if num1.isdigit() == True and num2.isdigit() == True:
    pass
else:
    raise ValueError

assert function in ['+','-','/','*'], 'Указано неверное действие'

def calc(num1,num2):
    if function == '+':
        return(int(num1)+int(num2))
    if function == '-':
        return(int(num1)-int(num2))
    if function == '/':
        try:
            return(int(num1)/int(num2))
        except:
            print('Нельзя делить на ноль')
            raise ZeroDivisionError
    if function == '*':
        return(int(num1)*int(num2))

try:
    print('Ответ:', calc(num1,num2))
except:
    raise ValueError

# Задача №3
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "5465656",},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def names_list():
    print('СПИСОК ИМЕН')
    for i in documents:
        try:
           print(i['name'])
        except:
            print((f'Имя не найдено в документе {i}'))

names_list()

