'''
Faça um programa de lista telefonica.
Neste programa:
1- O usuário insere uma quantidade de nomes da preferencia dele
2- Para cada nome, um telefone deve ser inserido.
3- Após o término das inserções o programa deve entrar em um loop onde o usuário insere o nome de uma pessoa e obtém o telefone dela.
Dica: utilize o método index de listas
'''
nomes = []
telefones = []
n = int(input('Quantos números você quer cadastrar? '))

for i in range (n):
    nome = input(f'Insira o nome {i + 1}:')

    telefone = input(f'Insira o número de telefone {i + 1}(Sem caractéres especiais): ')
    while len(telefone) < 8 or len(telefone) > 9:
        print('Tamanho do número de telefone inválido!Tente novamente.')
        telefone = input('Insira o número de telefone: ')
        
    nomes.append(nome)
    telefones.append(telefone)

while True:
    encontrar = input('Informe o nome da pessoa qual você quer ver o telefone: ')
    try:
        indice = nomes.index(encontrar)
        numero = telefones[indice]
        print(f'O telefone de {encontrar} é {numero}')
    except ValueError as ex:
        print('Deu ruim!')
