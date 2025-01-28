'''
Faça um programa de lista telefonica.
Neste programa:
1- O usuário insere uma quantidade de nomes da preferencia dele
2- Para cada nome, um telefone deve ser inserido.
3- Após o término das inserções o programa deve mostrar uma lista telefonica (com todos os nomes e números inseridos)
'''
nomes = []
telefones = []
numeros_inserios = int(input('Quantos números você quer cadastrar? '))

for i in range (numeros_inserios):
    nome = input('Insira o nome:')

    telefone = input('Insira o número de telefone (Sem caractéres especiais): ')
    while len(telefone) < 8 or len(telefone) > 9:
        print('Tamanho do número de telefone inválido!Tente novamente.')
        telefone = input('Insira o número de telefone: ')
        
    nomes.append(nome)
    telefones.append(telefone)

for i in range(numeros_inserios):
    print(f'{nomes[i]} : {telefones[i]}')