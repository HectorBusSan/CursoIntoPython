new_planet=''
planets=[]

while new_planet != 'done':
    new_planet= input('Introduce un nombre de un planeta ')
    if(new_planet!='done'):
        planets.append(new_planet.title())

for item in planets:
    print(item)
