nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

assert idade >= 0, 'Error: idade menor que zero!'
"""if idade < 0:
    print('Idade inválida')
   exit()  
 """   
if idade >=60:
    print(f'{nome} é idoso!')
elif idade >= 18:
    print(f'{nome} é adulto!')
elif idade >= 12:
    print(f'{nome} é adolescente!')
else:
    print(f'{nome} é criança!')

print(f'{nome} tem {idade} anos de idade!')