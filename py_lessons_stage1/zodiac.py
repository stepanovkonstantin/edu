month = input('Введите месяц:')
day = int(input('Введите число:'))
print ('Ваш знак зодиака:')

if month == 'январь':
    if day <= 21:
        print ('Козерог')
    else:
        print('Водолей')

elif month == 'февраль':
    if day <= 18:
        print ('Водолей')
    else:
        print('Рыбы')

elif month == 'март':
    if day <= 20:
        print ('Рыбы')
    else:
        print('Овен')

elif month == 'апрель':
    if day <= 20:
        print ('Овен')
    else:
        print('Телец')

elif month == 'май':
    if day <= 20:
        print ('Телец')
    else:
        print('Близнецы')

elif month == 'июнь':
    if day <= 20:
        print ('Близнецы')
    else:
        print('Рак')

elif month == 'июль':
    if day <= 22:
        print ('Рак')
    else:
        print('Лев')

elif month == 'август':
    if day <= 22:
        print ('Лев')
    else:
        print('Дева')

elif month == 'сентябрь':
    if day <= 23:
        print ('Дева')
    else:
        print('Весы')

elif month == 'октябрь':
    if day <= 23:
        print ('Весы')
    else:
        print('Скорпион')

elif month == 'ноябрь':
    if day <= 21:
        print ('Скорпион')
    else:
        print('Стрелец')

elif month == 'декабрь':
    if day <= 21:
        print ('Стрелец')
    else:
        print('Козерог')
