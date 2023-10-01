# Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной


def write_name():
    name = input('Введите имя: ')
    return name


def write_surname():
    surname = input('Введите фамилию: ')
    return surname


def write_phone():
    phone = input('Введите телефон: ')
    return phone


def write_adress():
    adress = input('Введите адрес: ')
    return adress

def input_data(a=None):
    name = write_name()
    surname = write_surname()
    phone = write_phone()
    adress = write_adress()
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(f'{name} {surname}: {phone}\n{adress}\n\n')


def print_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        print(data)
        data_first = data.readlines()
        print(data_first)
        for line in data_first:
            print(line, end='')


def search_line():
    search = input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        print(data)
        temp = data.readlines()
        print(temp)
        data_first = ''.join(temp).split('\n\n')
        print(data_first)
        for line in data_first:
            if search in line:
                print(line)








# input_data()
# print_data()
# search_line()