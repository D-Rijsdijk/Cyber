peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em m: '))

imc = peso / altura **2

if imc < 15:
    print(f'O seu imc é igual a {imc:.2f} e você está com magreza extrema.')
elif imc >= 15 and imc < 18.55:
    print(f'O seu imc é igual a {imc:.2f} e você está abaixo do peso.')
elif imc >= 18.55 and imc < 24.95:
    print(f'O seu imc é igual a {imc:.2f} e você está com peso normal.')
elif imc >= 24.95 and imc < 29.95:
    print(f'O seu imc é igual a {imc:.2f} e você está acima do peso.')
elif imc >= 29.95 and imc < 39.95:
    print(f'O seu imc é igual a {imc:.2f} e você está com obesidade grau I.')
else:
    print(f'O seu imc é igual a {imc:.2f} e você está com obesidade grau II.')