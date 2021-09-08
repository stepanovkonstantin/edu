import random

words_bank = ['радость', 'брынза', 'правовед', 'разница', 'былина', 'управление', 'костоправ', 'новичок', 'автомобил', 'динозавр', 'выхухоль', 'машажопа', 'заложник', 'вагонка']
secret_word = random.choice(words_bank)

user_word = ['*'] * len(secret_word)
user_word: str = ''.join(user_word)
print("Угадайте слово:", user_word)
user_word = ['*'] * len(secret_word)

miss = 0
while True:

    letter = input("Введите букву > ")
    if letter in secret_word:
        for pos, symbol in enumerate(secret_word):
            if symbol == letter:
                user_word[pos] = letter
        if '*' not in user_word:
            print('Вы выиграли!')
            print('Всего ошибок: ', miss)
            break
    else:
        miss += 1
        print('Ошибок допущено: ', miss)
    print(''.join(user_word))

