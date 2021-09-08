boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Anton']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) != len(girls):
  print('Различное кол-во парней и девушек невозможно познакомить!')
else:
  sorted_pairs = zip(sorted(boys),sorted(girls))
  print('Идеальные пары:')
  for pair_boy, pair_girl in sorted_pairs:
    print(f'{pair_boy} и {pair_girl}')
