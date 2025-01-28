'''
Faça um programa de cadastramento de pessoas. Esee programa deve ter um menu com as seguintes opções:

1 - Cadastrar pessoa.
2 - Listar cadastros.
3 - Salvar cadastros.
4 - Carregar cadastros.

Na opção 1, o usuário isere dados da pessoa (nome e cpf). A pessoa é, então, registrada em uma tabela formada por 
coleção de dados.

Na opção 2, o programa mostra todos os cadastros no terminal.

Na opção 3, o programa salva os cadastros em um arquivo JSON.

Na opção 4, o programa abre o arquivo JSON e carrega os cadastros.
'''

import json

tabela = {
    'nome': [],
    'cpf': []
}

while True:
    print("---Menu---")
    print("1 - Cadastrar pessoa.")
    print("2 - Listar cadastros.")
    print("3 - Salvar cadastros.")
    print("4 - Carregar cadastros.")
    print("5 - Sair")
    op = int(input("Escolha uma opção: "))
    
    if op == 1:
        nome = input('Nome: ')
        cpf = input('CPF: ')
        tabela['nome'].append(nome)
        tabela['cpf'].append(cpf)
    elif op == 2:
        n = len(tabela['nome']) #Quantidade de cadastros
        for i in range(n):
            nome = tabela['nome'][i]
            cpf = tabela['cpf'][i]
            print(f"Nome: {nome}, CPF: {cpf}")
    elif op == 3:
        with open('cadastros.json', 'w') as f:
            f.write(json.dump(tabela))
    elif op == 4:
        with open('cadastros.json', 'r') as f:
            conteudo = f.read()
            tabela = json.loads(conteudo)
    elif op == 5:
        break
    else:
        print("Opção inválida. Tente novamente.")
    
    