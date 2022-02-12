Mercurio=	57900000
Venus=	108200000
Tierra=	149600000
Marte=	227900000
Júpiter=	778600000
Saturno=	1433500000
Urano=	2872500000
Neptuno=	4495100000

print('''Escoja un numero cada numero es un planeta el planeta:
1= Mercurio
2= Venus
3= Tierra
4= Marte
5= Júpiter
6= Saturno
7= Urano
8= Neptuno''')
sol= input('Selecciona: ')
sol= int(sol)
if(sol == 1):
    millas= abs(Mercurio * .621)
    print(round(millas))
elif(sol == 2):
    millas= abs(Venus * .621)
    print(round(millas))
elif(sol == 3):
    millas= abs(Tierra * .621)
    print(round(millas))
elif(sol == 4):
    millas= abs(Marte * .621)
    print(round(millas))
elif(sol == 5):
    millas= abs(Júpiter * .621)
    print(round(millas))
elif(sol == 6):
    millas= abs(Saturno * .621)
    print(round(millas))
elif(sol == 7):
    millas= abs(Urano * .621)
    print(round(millas))
elif(sol == 8):
    millas= abs(Neptuno * .621)
    print(round(millas))
else:
    print('planeta no encontrado')
