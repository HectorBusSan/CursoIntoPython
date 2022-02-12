planets=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
name=input('Nombre del planeta ')
buscar= planets.index(name)
input(f'Planeta numero {buscar}')
input('apartir de este planeta los siguientes planetas son estan mas cerca del sol')
input(planets[0:buscar])
