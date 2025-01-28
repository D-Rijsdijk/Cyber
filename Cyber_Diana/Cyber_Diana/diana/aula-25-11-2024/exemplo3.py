#Lista de nomes
nomes = ['Filipe', 'Raquel', 'Fabrício', 'Diana', 'Guilherme']

#De trás pra frente
for i in range(len(nomes)-1,0,-1):
    nome = nomes[i]

"""
 Outra forma
for i in range(len(nomes)):
    nome = nomes[len(nomes)-i-1]
    print(nome)
"""