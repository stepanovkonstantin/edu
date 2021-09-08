documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def person(documents_list):
    doc_num= input('Введите номер документа > ')
    for document in documents_list:
        if doc_num == document["number"]:
            print(f'Документ на имя : {document["name"]}')
    return

def shelf(directories_list):
    doc_num = input('Введите номер документа > ')
    res_status = False
    for dir_num, dir_values in directories_list.items():
        if doc_num in dir_values:
            print(f'Документ находится на полке # {dir_num}')
            res_status = True
    return res_status

def list(documents_list):
    for doc_item in documents_list:
        print(f'{doc_item["type"]} "{doc_item["number"]}" "{doc_item["name"]}"')
    return

def add(documents_list, directories_list):
    add_type = input('Введите тип документа > ')
    add_number = input('Введите номер документа > ')
    add_name = input('Введите имя > ')
    add_shelf_num = input('Введите номер полки для документа > ')
    if add_shelf_num in directories_list.keys():
        directories_list[add_shelf_num].append(add_number)
        documents_list.append(dict(type=add_type, number=add_number, name=add_name))
    else:
        print('Указана несуществующая полка для документа!')
    return

def remove_from_shelf(doc_number, directories_list):
    res_status = False
    for dir_num, dir_values in directories_list.items():
        if doc_number in dir_values:
            directories_list[dir_num].remove(doc_number)
            res_status = True
    return res_status

def delete(documents_list, directories_list):
    del_number = input('Введите номер документа > ')
    res_status = False
    for document in documents_list:
        if del_number == document["number"]:
            documents_list.remove(document)
            res_status = True
    remove_from_shelf(del_number, directories_list)
    return res_status

def move(documents_list, directories_list):
    doc_number = input('Введите номер документа > ')
    shelf_number = input('Введите номер полки для перемещения документа > ')
    if shelf_number in directories_list.keys():
        if remove_from_shelf(doc_number, directories_list) == False:
            print('Документ с таким номером не существует!')
        else:
            directories_list[shelf_number].append(doc_number)
    else:
        print('Нельзя переместить документ на несуществую полку!')
    return

def add_shelf(directories_list):
    new_shelf_number = input('Введите номер новой полки > ')
    if new_shelf_number not in directories_list.keys():
        directories_list[new_shelf_number] = []
    else:
        print('Полка с таким номером уже существует!')
    return

def main(documents_list, directories_list):
    help = {
      'l': 'Вывод списка документов',
      'p': 'Поиск имени владельца по номеру документа',
      's': 'Поиск номера полки для существующего документа',
      'a': 'Добавление в каталог нового документа',
      'd': 'Удаление документа из каталога',
      'm': 'Перемещение документа между полками',
      'as': 'Создание новой полки в каталоге',
      'h': 'Вывод справки по командам',
      'e': 'Выход из программы'
    }
    print('------------------------------------------------')
    print('ПРОГРАММА ДЛЯ РАБОТЫ С КАТАЛОГОМ ДОКУМЕНТОВ')
    print('------------------------------------------------')
    print('Для вызова списка команд введите - h\n')

    while True:
        user_choise = input('Введите команду > ')
        if user_choise == 'p':
            print('# Поиск владельца документа по номеру')
            person(documents_list)
        elif user_choise == 's':
            print('# Поиск полки по номеру документа')
            if shelf(directories_list) == False:
                print("Документ с таким номером не найден!")
        elif user_choise == 'l':
            print('# Список всех зарегистрированных документов')
            list(documents_list)
        elif user_choise == 'a':
            print('# Добавление нового документа')
            add(documents_list, directories_list)
        elif user_choise == 'd':
            print('# Удаление документа из базы')
            if delete(documents_list, directories_list) == False:
                print("Документ с таким номером не найден!")
        elif user_choise == 'm':
            print('# Перемещение документа между полками')
            move(documents_list, directories_list)
        elif user_choise == 'as':
            print('# Добавление новой полки в базу')
            add_shelf(directories_list)
        elif user_choise == 'h':
            for cmd, cmd_desc in help.items():
                print(f'{cmd} \t- {cmd_desc}')
        elif user_choise == 'e':
            print('ЗАВЕРШЕНИЕ ПРОГРАММЫ!')
            print('\n\nСодержание каталога документов:')
            print(documents_list)
            print(directories_list)
            break
        else:
            print('Введена неверная команда!')

main(documents, directories)
