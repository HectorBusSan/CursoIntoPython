# planet_moons = {
#     'mercury': 0,
#     'venus': 0,
#     'earth': 1,
#     'mars': 2,
#     'jupiter': 79,
#     'saturn': 82,
#     'uranus': 27,
#     'neptune': 14,
#     'pluto': 5,
#     'haumea': 2,
#     'makemake': 1,
#     'eris': 1
# }

planets_moons={}
button= ''
while button!= 'done':
    planet= input('Planeta: ')
    planet= planet.lower()
    moon= input('lunas del planeta ')
    planets_moons[planet]=int(moon)
    button= input('done para terminar enter seguir ')
# print(planets_moons)

planets= len(planets_moons.keys())
print(f"El numero de planetas es: {planets}")
for item in planets_moons.keys():
    print(item)

values_total=0
for value in planets_moons.values():
    values_total= values_total + value
print(f'Total de lunas:{values_total}')


