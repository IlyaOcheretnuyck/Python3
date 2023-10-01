from logger import *


def interface():
    command = 0
    while command != '6':
        print('''Что вы хотите сделать?
         1 - запись данных
         2 - вывод данных
         3 - поиск данных
         4 - внести изменения
         5 - удаление
         6 - выход''')
        command = input('Введите номер операции: ')
        while command not in ('1', '2', '3', '4', '5', '6'):
            print('Введите корректную команду!')
            command = input('Введите номер операции: ')

        if command == '1':
            input_data()
        elif command == '2':
            print_data()
        elif command == '3':
            search_line()
        elif command == '4':
            rewrite_line()
        elif command == '5':
            delete_data()