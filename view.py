from operator import index
from unicodedata import name


def menu():
    return int(input('''
        Выберите действие:
        1 - Добавить сведения по новому сотруднику в справочник;
        2 - Вывести справочник на экран;
        3 - Удалить все сведения по сотруднику;
        4 - Экспортировать справочник в файл;
        5 - Импортировать справочник из файла;
        6 - Изменение данных сотрудника;
        0 - Выход из справоника.
        введите номер:  '''))

def menu1():
    return (input('Введите полностью все данные через пробел:\n'))

def output_directory(lst_contact):
    print('id', 'фамилия', 'имя', 'год рождения',
          'должность')
    for value in lst_contact:
        print(lst_contact.index(value), value)
    

def input_contact():
    fam = input('Введите фамилию:')
    name = input('Введите имя:')
    year = input('Введите год рождения:')
    dol = input('Введите должность:')
    all_data = fam+' '+name+' '+year+' '+dol
    return all_data


def all_del_contact():
    return int(input('Введите номер удаляемой позиции справочника:\n'))


def editing_contact():
    return int(input('Выберите номер сотрудника в справочнике:'))
    
