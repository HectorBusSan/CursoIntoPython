# Ejercicio 1
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth.",
"On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
# print(text.split('.'))
text1=text.split('.')
palabras=['average', 'temperature', 'distance']
# print(text.find(palabras[0]))
# print(text.find(palabras[1]))
# print(text.find(palabras[2]))

for item in text1:
    for palabras in palabras:
        if palabras in item:
            print(item)
            print(item.replace('C','Celcius'))
        break

# Ejercicio 2
texto= """Gravity Facts about Ganymede
-------------------------------------------------------------------------------
Planet Name: Mars
Gravity on Ganymede: 1.4300000000000002 m/s2"""
name= "Moon"
gravity= .00162
planet= "Earth"
# dividir=texto.split('\n')
# print(dividir)
titulo= f'Gravedad en {name}'
# print(titulo)
datos= f"""{'-'*45}
Planeta: {planet}
Gravedad en {name}: {gravity*1000}m/s2"""
completo= f"""{titulo}
{datos}"""
# print(datos)
print(completo)
# ------------------------------------------
planeta = 'Marte '
gravedad  = 0.00143*1000
nombre = 'Ganímedes'
titulo2=f"""
Gravedad en {nombre}"""
completo2="""{titulo2}
Datos de Gravedad sobre: {nombre}
------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
informacion=(completo2.format(titulo2=titulo2,nombre=nombre,planeta=planeta,gravedad=gravedad))
print(informacion)
