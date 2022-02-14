from datetime import timedelta, datetime

def lanz(**lanzar):
    print('Informaición:')
    hora_de_lanzamiento= datetime.now()
    print(hora_de_lanzamiento.strftime('Lanzamiento %A %H:%M:%S'))
    for name, item in lanzar.items():
        print(f"""{name}: {item}""")

print(lanz(tiempo_de_vuelo=50, destino='Moon', tanque_externo=10, tanque_interno=10))
