set_countries = {'col', 'mex', 'bol'}

print(len(set_countries))

print('col' in set_countries)
print('cl' in set_countries)

set_countries.add('cl')
print(set_countries)

set_countries.update({'arg', 'ecua', 'cl'})
print(set_countries)

set_countries.remove('arg')
set_countries.discard('pe')
print(set_countries)

set_countries.clear()

print(len(set_countries))
