# Статистика текста

letters = dict()
replacements = [('  ', ' '),
                ('   ', ' '),
                (' - ', ' '),
                (' — ', ' '),
                (' & ', ' '),
                ('... ', '. ')]

def replace(str_value, old_new):
  for vals in old_new:
    old, new = vals
    str_value = str_value.replace(old, new)
  return str_value

str_user = input('Введите строку:\n> ').lower()
str_edited = replace(str_user, replacements)

for sign in str_edited:
  if sign in letters:
    letters[sign] += 1
  else:
    letters[sign] = 1

noreads = list(',’@#$%^&*\(\)-_+={}/<>:;"0123456789°')
for noread in noreads:
  letters.pop(noread, '')

print ('')
snt_ends = ('.', '!', '?')
sentences = [letters.get(key, 0) for key in snt_ends]
print ('Количество предложений: ', sum(sentences))
spaces = letters.get(' ', 0)
print ("Количество слов: ", spaces + 1)
print ('Статистика символов введенной строки:')

noreads = list(" .!?'")
for noread in noreads:
  letters.pop(noread, '')

sort_d = dict([(k, letters[k]) for k in sorted(letters, key=letters.get, reverse=True)])
for k in sort_d:
  print (k, ":", sort_d[k])
