'''
Faça um programa de lista de nomes.
Nesse programa, o usuário deve informar 10 nomes.
Os nomes devem ser inseridos em uma lista, e, em seguida, o programa deve mostrar 10 nomes inseridos
'''
nomes = []

for i in range(10):
    nomes.append(input('Insira um nome: '))
    
for i in range(10):
    print(nomes[i])
 