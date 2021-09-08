list_example = ['2018-01-01', 333, 'andywarhole', 'yandex', 'fixed', 'cpc', 'a', 'idd', 100]
dict_example = dict()
# print(list_example, '\n')

while len(list_example) > 2:
    dict_key_curr = list_example[-2]
    dict_val_curr = list_example[-1]
    dict_curr = {dict_key_curr: dict_val_curr}
    list_example.pop()
    list_example.pop()
    list_example.append(dict_curr)

dict_example[list_example[0]] = list_example[1]
print(dict_example)