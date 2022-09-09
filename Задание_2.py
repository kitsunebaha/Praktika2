states = {
 'Россия': 'RU',
 'Германия': 'DE',
 'Узбекистан': 'UZ',
 'Зимбабве': 'ZW',
 'Турция': 'TR'
 }

 # создание базового набора стран и некоторых городов в них
cities = {
 'UZ': 'Газли',
 'TR': 'Сарыгерме',
 'DE': 'Мюнхен'
 }

 # добавление нескольких городов
cities['ZW'] = 'Гверу'
cities['RU'] = 'Москва'

# вывод некоторых городов
print ( ' - ' * 10)
print ( " B стране ZW есть город: ", cities['ZW'])
print (" В стране RU есть город: ", cities['RU'])

 # вывод некоторых стран
print ( ' - ' * 10 )
print ("Аббревиатура Турции: ", states['Турция'])
print("Аббревиатура Германии: ", states['Германия'])

# выполняется с учетом страны и словаря городов
print ('-' * 10 )
print ("В Турции есть город: ", cities[states['Турция']])
print ("В Германии есть город: ", cities[states['Германия']])

 # вывод аббревиатур всех стран
print ('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} имеет аббревиатуру {abbrev}")


print('-' * 10)
for abbrev, city in list(cities.items()):
     print(f"B стране {abbrev} есть город {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
     print(f"B стране {state} используется аббревиатура {abbrev}")
     print(f"И есть город {cities[abbrev]}")

print('-' * 10)
state = states.get('СССP')

if not state:
      print("npoшу прощения, СССР распался.")