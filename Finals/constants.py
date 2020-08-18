from time import sleep
from functools import partial

SLEEP = partial(sleep, 0.34)
MENU_TEXT_MAIN = '''***********************
Введите: 
1 - чтобы сохранить результат поиска в файл
2 - чтобы перейти к следующей странице
quit - чтобы завершить программу
ВАШ ВЫБОР:'''
ACCEPTABLE_ANSWERS = ['1','2', 'quit']
SEPARATOR = '***********************'