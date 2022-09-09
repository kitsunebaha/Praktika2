group = {
    'dkmo-21': 'Технология разработки',
    'dkms-21': 'Разработка программных модулей',
    'dkmo -22': 'Разработка мобильных приложений',
    'dkmo -22/1': 'Тестирование программного обеспечения'
}
print( group['dkms-21'] )
for key in group.values():
    print( key )
newGroup = 'dkmo -22/2'
newDisciplineValue = 'Разработка баз данных'
if newGroup in group:
    print( 'Ok' )    
else:
    group[ newGroup ] = newDisciplineValue
print( group )
{'dkmo-21': 'Технология разработки', 'dkms-21': 'Разработка программных модулей', 'dkmo -22': 'Разработка мобильных приложений', 'dkmo -22/1': 'Тестирование программного обеспечения', 'dkmo -22/2': 'Разработка баз данных'}
group.setdefault('dkems-21', 'Системы облачного хранения')
for key in group.values():
    print( key )