queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
queries_num = len(queries)
queries_analyse = dict()
words_num = 0
for query in queries:
    words_num = 0
    for sign in query:
        if sign == ' ':
            words_num += 1
    words_num += 1
    if words_num in queries_analyse:
        queries_analyse[words_num] += 1
    else:
        queries_analyse[words_num] = 1
print('Распределение запросов по кол-ву слов:')
for key in queries_analyse:
    analysed_perc = queries_analyse[key] / queries_num * 100
    print(f'{key} слов в запросах: {analysed_perc :f}%')
