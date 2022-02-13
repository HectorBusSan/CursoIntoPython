planets={
    'name': 'Mars',
    'moons': 2
}
print(f"Planeta: {planets.get('name')} tiene {planets['moons']} lunas")

planets['circunferencia']={
    'polar': 6752,
    'equatorial': 6792
}
# print(planets)
print(f"planeta:{planets['name']}, Diametro polar: {planets['circunferencia']['polar']}")
