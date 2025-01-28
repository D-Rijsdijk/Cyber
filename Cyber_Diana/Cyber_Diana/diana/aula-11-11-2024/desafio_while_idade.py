idade = int(input('Insira uma idade: '))

while True:
    if idade > 0:
        break
    print('Idade inválida! Tente novamente.')
    idade = int(input('Insira uma idade: '))

print(f'A idade é {idade}')