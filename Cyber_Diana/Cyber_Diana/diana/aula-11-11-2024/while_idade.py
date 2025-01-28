idade = int(input('Insira sua idade: '))

while idade < 0:
    print('Idade inválida, tente novamente.')
    idade = int(input('Insira sua idade: '))
print(f'A idade é {idade}')
