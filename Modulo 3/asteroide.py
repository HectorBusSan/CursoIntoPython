## Asteroides:
dimensión= input('dimensión ')
# print(dimensión)
velocidad= input('velocidad del asteroide ')
# print(velocidad)
velocidadT= input('Velocidad de entrada en la tierra ')
if(int(dimensión)>25 and int(dimensión)<1000):
    print('Asteroide muy peligroso para la tierra')
elif(int(velocidad)>25):
    print('Velocidad peligrosa ¡Advertencia!')
elif(int(velocidadT)>=20):
    print('Velocidad capaz de verse un rayo desde la tierra')
else:
    print('no hay peligro')
