temp = float(input('informe a temperatura atual (ºC): '))

if temp < 20:

    print('Está frio')

elif temp > 20 and temp < 30:

    print('Está fresco')

elif temp > 30 and temp < 36:

    print('Está quente')

else:

    print('Está muito quente')