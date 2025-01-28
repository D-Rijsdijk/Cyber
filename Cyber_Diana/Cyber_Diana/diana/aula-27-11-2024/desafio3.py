'''
Implemente a função pegar_nomes de modo que:
1-- ela peça para o usuário digitar uma série de nomes.
    obs:quem decide quantos nomes é o usuário.
2-- ela retorna uma tupla com a lista de nomes e a quantidade de nomes inseridos.
'''

def pegar_nomes():
    lista_nomes = []
    n = int(input('Quantos nomes deseja inserir? '))
    for i in range(n):
        nome = input(f'{i+1} nome: ')
        lista_nomes.append(nome)
    return lista_nomes, n

nomes, qtd_nomes = pegar_nomes()

for i in range(qtd_nomes):
    print(f'{i} | {nomes[i]}') 