#Lista de nomes
nomes = ['Filipe', 'Raquel', 'Fabrício', 'Diana', 'Guilherme']

print('-- Antes do append --')
for i in range(len(nomes)):
    nome = nomes[i]
    print(nome) # Pode substituir o nome = nomes[i] simplesmente pelo print(nomes[i])

nomes.append('Lucas') #Insere 'Lucas' no fim da fila

print('-- Depois do append --')
for i in range(len(nomes)):
    print(nomes[i])

nomes.pop(0) #Remove o elemento 0

print('-- Depois do pop --')
for i in range(len(nomes)):
    print(nomes[i])

nomes.remove('Guilherme') #Remove o Guilherme da lista

print('-- Depois do remove--')
for i in range(len(nomes)):
    print(nomes[i])