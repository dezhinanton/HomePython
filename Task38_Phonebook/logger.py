import os
from data_create import name_data,surname_data,phone_data,second_name_data
file_name = 'Task38_Phonebook/data.txt'


def print_data():
    if os.path.exists(file_name):
        print('Вывод данных из файла:')
        print()
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines() 
            for line in list_data:
                print(line)
    else:
        print('Файл не существует!')


def input_data():
    print('Введите данные:')
    surname = surname_data()
    name = name_data()
    second_name = second_name_data()
    phone = phone_data()
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{surname};{name};{second_name};{phone}\n') 
        

def find_data(find_string):
    if os.path.exists(file_name):
        print()
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines()
            find_count = 0
            found_index = []
            find_string = find_string.lower()
            for i in range(len(list_data)):
                line = list_data[i].lower()
                if find_string in line:
                    print(i, line)
                    find_count +=1
                    found_index.append(i)
            if find_count == 0:
                print('Ничего не найдено!')
            else:
                print()
                print(f'Найдено: {find_count} записей')
    else:
        print('Файл не существует!')
    return found_index


def delete_data(delete_string):
    index_list = find_data(delete_string)
    if not len(index_list):
        print('Нет данных для удаления')
    else:
        print('Введите номера записей для удаления через пробел: ')
        list_to_delete = list(map(int, (input().split())))
        list_to_delete.sort(reverse=True)
        if len(list_to_delete):
            with open(file_name, 'r', encoding='utf-8') as file:
                list_data = file.readlines()
                for ind_to_del in list_to_delete:
                    if ind_to_del in index_list:
                        list_data.pop(ind_to_del)
                    else:
                        print('Введен неверный индекс ')
            with open(file_name, 'w', encoding='utf-8') as file:
                file.writelines(list_data)
            print('готово')
        else:
            print('не были выбраны строки. выход из режима удаления')


def change_data(change_string):
    index_list = find_data(change_string)
    if not len(index_list):
        print('Нет данных для изменения')
    else:
        print('Введите номер записи для редактирования: ')
        str_to_change = int(input())
        if str_to_change in index_list:
            with open(file_name, 'r', encoding='utf-8') as file:
                list_data = file.readlines()
                line_to_chng = list_data[str_to_change].split(';')
                print(line_to_chng)
                print("""Доступные команды: 
                        1 - редактировать фамилию
                        2 - редактировать имя
                        3 - редактировать отчество 
                        4 - редактировать телефон
                        5 - выйти из режима редактирования 
                        """)
                number = 0 
                while number != 5:
                    number = 0
                    while number < 1 or number > 5:
                        print('Введите номер команды: ')
                        number = int(input())
                    if number == 1:
                        print('Введите новую фамилию: ')
                        line_to_chng[0] = input()
                    elif number == 2:
                        print('Введите новое имя: ')
                        line_to_chng[1] = input()
                    elif number == 3:
                        print('Введите новое отчество: ')
                        line_to_chng[2] = input()
                    elif number == 4:
                        print('Введите новый телефон: ')
                        phone = input()
                        line_to_chng[3] = phone + '\n'
                list_data.pop(str_to_change)
                list_data.append(';'.join(line_to_chng))
            with open(file_name, 'w', encoding='utf-8') as file:
                file.writelines(list_data)
                print()
                print('готово!')
        else:
            print('Введен неверный индекс ')