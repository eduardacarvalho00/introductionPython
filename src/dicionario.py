planet = {
    'name': 'Earth',
    'moons': 1
}
print(planet['name'])
print(planet.get('name'))
# Displays Earth

planet.update({'name': 'Makemake'})
planet.update({
    'name': 'Jupiter',
    'moons': 79
})
planet['name'] = 'Makemake'
# name is now set to Makemake


planet['orbital period'] = 4333

# remover uma chave
planet.pop('orbital period')

planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}


rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
# Output:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
# Because december exists, the value will be 3.1


total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')
# Output:
# There was 10.8cm in the last quarter
