# Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

from data_create import *


def input_data(a=None):
    name = write_name()
    surname = write_surname()
    phone = write_phone()
    adress = write_adress()
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(f'{name} {surname}: {phone}\n{adress}\n\n')


def print_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        data_first = data.readlines()
        for line in data_first:
            print(line, end='')


def search_line():
    search = input('Введите данные для поиска: ')
    search = search.capitalize()
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        temp = data.readlines()
        data_first = ''.join(temp).split('\n\n')
        for line in data_first:
            if search in line:
                print(line)
        return line


def rewrite_line():
    search_line()
    rewrite_name = input('Введите заменяемое значение: ')
    new_name = input('Введите новое значение: ' + ':')
    with open('phonebook.txt', 'r', encoding='utf-8') as text:
        old_data = text.read()
        new_data = old_data.replace(rewrite_name, new_name)
    with open('phonebook.txt', 'w', encoding='utf-8') as text:
        text.write(new_data)


def delete_data():
    search_line()
    rewrite_name = input('Введите заменяемое значение: ')
    rewrite_name = rewrite_name.capitalize()
    delete = ''
    with open('phonebook.txt', 'r', encoding='utf-8') as text:
        old_data = text.read()
        new_data = old_data.replace(rewrite_name, delete)
    with open('phonebook.txt', 'w', encoding='utf-8') as text:
        text.write(new_data)

# input_data()
# print_data()
# search_line()