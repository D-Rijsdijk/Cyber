kg_ou_g = input('Você gostaria de informar seu peso em kg ou g? ').lower()
peso = float(input('Informe seu peso: '))
m_ou_cm = input('Você gostaria de informar sua altura em m ou cm? ').lower()
altura = float(input('Informe sua altura: '))

if kg_ou_g == 'g' or kg_ou_g == 'kg':
    if kg_ou_g == 'g':
        peso = peso / 1000
else:
    print('Unidade de peso inválida!')
    exit()

if m_ou_cm == 'cm' or m_ou_cm == 'm':
    if m_ou_cm == 'cm':
        altura = altura / 100
else:
    print('Unidade de altura inválida!')
    exit()

imc = peso / altura**2

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