def tanques_gasolina(**kwan):
    longitud= len(kwan)
    i=0
    litros=0
    for title, item in kwan.items():
        # print(item)
        litros= litros + item
        print(title)
    prom=(litros)/longitud
    print(f'El promedio de los {longitud} tanques es: {prom}')

tanques_gasolina(tanque1=10, tanque2=20, tanque3=30)

def tanques(tanques):
    longitud = len(tanques)
    total = sum(tanques)/longitud

    print(f'El promedio de los tres tanques es: {total}')

tanques([10,20,30])
