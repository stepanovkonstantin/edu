def person(documents_list):
    doc_num = input('Введите номер документа > ')
    res_status = False
    for document in documents_list:
        if doc_num == document["number"]:
            print(f'Документ на имя : {document["name"]}')
            res_status = True
    return res_status

def shelf(directories_list):
    doc_num = input('Введите номер документа > ')
    shelf_num = shelf_by_number(directories_list, doc_num)
    if shelf_num == None:
        return False
    else:
        print(f'Документ находится на полке # {shelf_num}')
        return True

def shelf_by_number(directories_list, doc_num):
    shelf_found = None
    for dir_num, dir_values in directories_list.items():
        if doc_num in dir_values:
            shelf_found = dir_num
    return shelf_found

def search_by_type(documents_list, directories_list):
    doc_type = input('Введите тип документа > ')
    docs_count = 0
    for document in documents_list:
        if document["type"] == doc_type:
            shelf_num = shelf_by_number(directories_list, document["number"])
            print(f'# {shelf_num}: \t"{document["number"]}"\t\t{document["name"]}')
            docs_count += 1
    return docs_count

def list_shelf(documents_list, directories_list):
    shelf_num = input('Введите номер полки > ')
    docs_count = 0
    if shelf_num not in directories_list.keys():
        print('Полка с таким номером не существует!')
    else:
        for doc_num in directories_list[shelf_num]:
            for document in documents_list:
                if document["number"] == doc_num:
                    print(f'{document["type"]} \t"{document["number"]}" \t{document["name"]}')
            docs_count += 1
    return docs_count

def shelf_count(directories_list):
    docs_count = 0
    for dir_num, dir_values in directories_list.items():
        print(f'{dir_num}: {len(dir_values)} документа')
        docs_count = docs_count + len(dir_values)
    return docs_count


def list_docs(documents_list):
    for doc_item in documents_list:
        print(f'{doc_item["type"]} \t"{doc_item["number"]}" \t"{doc_item["name"]}"')
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

def list_docs_by_numbers(documents_list, *doc_numbers):
    foundcount = 0
    print('Результаты поиска :')
    for doc_num in doc_numbers:
        isfound = False
        for document in documents_list:
            if doc_num == document["number"]:
                print(f'"{document["number"]}"\t{document["type"]}\t\t{document["name"]}')
                isfound = True
                foundcount += 1
        if isfound == False:
            print(f'"{doc_num}" не найден')
    return foundcount

def read_docs_file(doc_file):
    documents_input = open(doc_file, 'r+')
    documents_list = []
    for line in documents_input.readlines():
        linenoend = line.replace('\n', '')
        doc_split = list(linenoend.split(','))
        doc_dict = dict(type=doc_split[0], number=doc_split[1], name=doc_split[2])
        documents_list.append(doc_dict)
    documents_input.close()
    return documents_list

def read_dir_file(dir_file):
    directories_input = open(dir_file, 'r+')
    directories_list = {}
    for line in directories_input.readlines():
        linenoend = line.replace('\n', '')
        dir_split = list(linenoend.split(','))
        directories_list[dir_split[0]] = dir_split[1:]
    directories_input.close()
    return directories_list

def save_to_files(documents_list, doc_file, directories_list, dir_file):
    docs_count = 0
    documents_out = open(doc_file, "w")
    for document in documents_list:
        wline = document["type"] + "," + document["number"] + "," + document["name"] + "\n"
        documents_out.write(wline)
        docs_count += 1
    documents_out.close()
    directories_out = open(dir_file, "w")
    for dir_num, dir_values in directories_list.items():
        doc_str = ''
        for doc_num in dir_values:
            doc_str = doc_str + "," + doc_num
        wline = dir_num + doc_str + "\n"
        directories_out.write(wline)
    directories_out.close()
    return docs_count

def main(catalogue):
    help = {
      'l': ['list', 'Вывод списка документов'],
      'i': ['index', 'Вывести список номеров полок'],
      'v': ['view', 'Вывести список документов по номеру полки'],
      't': ['type', 'Поиск документов по типу'],
      'p': ['person', 'Поиск имени владельца по номеру документа'],
      'n': ['number', 'Поиск номера полки для существующего документа'],
      'b': ['batch', 'Поиск документов по списку номеров'],
      'a': ['add', 'Добавление в каталог нового документа'],
      'd': ['del', 'Удаление документа из каталога'],
      'm': ['move', 'Перемещение документа между полками'],
      'c': ['create', 'Создание новой полки в каталоге'],
      'h': ['help', 'Вывод справки по командам'],
      's': ['save', 'Сохранить результат работы в файл'],
      'e': ['exit', 'Выход из программы']
    }
    print('-------------------------------------------------')
    print('ПРОГРАММА ДЛЯ РАБОТЫ С КАТАЛОГОМ ДОКУМЕНТОВ v.2.0')
    print('-------------------------------------------------')
    print('Для просмотра списка команд введите - h')
    doc_file = str(catalogue) + '_docs.txt'
    dir_file = str(catalogue) + '_dirs.txt'
    documents_list = read_docs_file(doc_file)
    directories_list = read_dir_file(dir_file)
    # if documents_list is None:
    #     documents_list = []
    # if directories_list is None:
    #     directories_list = {}

    user_choise = "h"
    while user_choise != "e":
        user_choise = input('\nВведите команду > ')
        if user_choise == 'p' or user_choise == 'person':
            print('# Поиск владельца документа по номеру')
            if person(documents_list) == False:
                print('Документ с таким номером не найден!')
        elif user_choise == 'n' or user_choise == 'number':
            print('# Поиск полки по номеру документа')
            if shelf(directories_list) == False:
                print('Документ с таким номером не найден!')
        elif user_choise == 'l' or user_choise == 'list':
            print('# Список всех зарегистрированных документов')
            list_docs(documents_list)
        elif user_choise == 'i' or user_choise == 'index':
            print('# Список существующих полок')
            docs_count = shelf_count(directories_list)
            print(f'Всего документов: {docs_count}')
        elif user_choise == 'v' or user_choise == 'view':
            print('# Поиск документов по номеру полки')
            docs_count = list_shelf(documents_list, directories_list)
            if docs_count == 0:
                print('Полка пуста!')
            else:
                print(f'Найдено {docs_count} документов')
        elif user_choise == 't' or user_choise == 'type':
            print('# Поиск документов по типу')
            docs_count = search_by_type(documents_list, directories_list)
            if docs_count == 0:
                print('Документы не найдены!')
            else:
                print(f'всего найдено: {docs_count} документов')
        elif user_choise == 'b' or user_choise == 'batch':
            user_input_docs = []
            print('Вводите номера документов по одному. Для запуска поиска введите - s :')
            while True:
                user_input_doc_num = input('> ')
                if user_input_doc_num == 's':
                    break
                else:
                    user_input_docs.append(user_input_doc_num)
            foundcount = list_docs_by_numbers(documents_list, *user_input_docs)
            if foundcount == 0:
                print('Ни одного документа не найдено!')
            else:
                print(f'Найдено {foundcount} документов')
        elif user_choise == 'a' or user_choise == 'add':
            print('# Добавление нового документа')
            add(documents_list, directories_list)
        elif user_choise == 'd' or user_choise == 'del':
            print('# Удаление документа из базы')
            if delete(documents_list, directories_list) == False:
                print("Документ с таким номером не найден!")
        elif user_choise == 'm' or user_choise == 'move':
            print('# Перемещение документа между полками')
            move(documents_list, directories_list)
        elif user_choise == 'c' or user_choise == 'create':
            print('# Добавление новой полки в базу')
            add_shelf(directories_list)
        elif user_choise == 's' or user_choise == 'save':
            print('\n# СОХРАНЕНИЕ ДАННЫХ В ФАЙЛЫ!')

            save_to_files(documents_list, doc_file, directories_list, dir_file)
        elif user_choise == 'h':
            for cmd, cmd_desc in help.items():
                print(f'{cmd} \t- {cmd_desc[1]}')
        elif user_choise == 'help':
            for cmd, cmd_desc in help.items():
                print(f'({cmd}) {cmd_desc[0]} \t- {cmd_desc[1]}')
        elif user_choise == 'e' or user_choise == 'exit':
            print('\nЗАВЕРШЕНИЕ ПРОГРАММЫ!')
            while True:
                saveyn = input('Сохранить данные? \n(y/n) > ')
                if saveyn == "y":
                    docs_count = save_to_files(documents_list, doc_file, directories_list, dir_file)
                    print(f'{docs_count} документов сохранено в каталоге')
                    break
                elif saveyn == "n":
                    break
                else:
                    print('Выберите y/n!')
            print('-------------------------------------------------')
        else:
            print('Введена неверная команда!')


catalog_name = "kstepanov"
catalog_path = "" + catalog_name
main(catalog_path)
