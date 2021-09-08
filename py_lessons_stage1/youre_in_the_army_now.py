height_dict = {'гном': '150', 'танкист': '160', 'связист': '170', 'летчик': '180', 'десантник': '190', 'космонавт': '200', 'баскеболист': '210'}

height = int(input('Введите рост:'))
age = int(input('Введите возраст:'))
children_num = int(input('Введите кол-во детей:'))
edu_now = input('Проходит ли обучение в университете сейчас (да/нет)? ')

if height > 210:
    print ('Слишком высок для армии!')

if edu_now == 'нет':
    if children_num < 2:
        if 18 <= age <= 27:
            for height_key in height_dict:
                if height < int(height_dict[height_key]):
                    print (height_key)
                    break
        else:
            print('Не подходит по возрасту!')
    else:
        print('Слишком много детей!')
else:
    print('Не подходит по возрасту!')




