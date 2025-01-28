#Lista de nomes
nomes = ['Filipe', 'Raquel', 'Fabrício', 'Diana', 'Guilherme']

#Esvaziar lista
for i in range(len(nomes)):
    print('Interação: ', i)
    nome_removido = nomes.pop()
    print('Nome removido: ', nome_removido)
    print('Lista atual: ', nomes)