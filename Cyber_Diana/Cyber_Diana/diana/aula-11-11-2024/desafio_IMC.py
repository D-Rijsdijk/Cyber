altura = float(input('Informe sua altura em m: '))
while altura < 0:
    print('Altura inválida!')
    altura = float(input('Informe sua altura em m: '))

peso = float(input('Informe seu peso em kg: '))
while peso < 0:
    print('Peso inválida!')
    peso = float(input('Informe seu peso em kg: '))

imc = peso / altura**2

if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso normal.')
else:
    print('Acima do peso.')



"""
EXISTE ESSA FORMA DE FAZER TAMBÉM, MAS É MAIS POLUÍDO
peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em m: '))

while True:
    if peso > 0 and altura > 0:
        imc = peso / altura **2
        if imc < 15:
            print(f'O seu imc é igual a {imc:.2f} e você está com magreza extrema.')
            break
        elif imc >= 15 and imc < 18.55:
            print(f'O seu imc é igual a {imc:.2f} e você está abaixo do peso.')
            break
        elif imc >= 18.55 and imc < 24.95:
            print(f'O seu imc é igual a {imc:.2f} e você está com peso normal.')
            break
        elif imc >= 24.95 and imc < 29.95:
            print(f'O seu imc é igual a {imc:.2f} e você está acima do peso.')
            break
        elif imc >= 29.95 and imc < 39.95:
            print(f'O seu imc é igual a {imc:.2f} e você está com obesidade grau I.')
            break
        else:
            print(f'O seu imc é igual a {imc:.2f} e você está com obesidade grau II.')
            break
    elif peso < 0 and altura < 0:
        print('Peso e altura inválidos! Tente novamente.')
        peso = float(input('Informe seu peso em kg: '))
        altura = float(input('Informe sua altura em m: '))
    elif peso < 0 and altura > 0:
        print('Peso inválido! Tente novamente.')
        peso = float(input('Informe seu peso em kg: '))
    else:
        print('Altura inválida! Tente novamente')
        altura = float(input('Informe sua altura em m: '))
"""
