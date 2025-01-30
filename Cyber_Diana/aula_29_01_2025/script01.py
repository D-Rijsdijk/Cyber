import json
import os
from tabulate import tabulate

#Caso não exista, cria a pasta cadastros
if not os.path.exists ('cadastros'):
        os.mkdir('cadastros')
        
while True:
    
    print('----Menu----')
    print('1. Cadastrar pessoa')
    print('2. Buscar cadastro')
    print('3. Listar cadastros')
    print('4. Deletar cadastro')
    print('5. Sair')
    
    op = input('Escolha uma opção: ')
    
    if op == '1': #'1. Cadastrar pessoa'(nome, email, telefone e CPF sem pontos)
        nome = input('Nome: ')
        email = input('Email: ')
        telefone = input('Telefone: ')
        cpf = input('CPF (Sem pontos): ')
        pessoa = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'cpf': cpf
        }
        with open(f'Cadastros/{cpf}.json', 'w') as f:
            pessoa_json = json.dumps(pessoa)
            f.write(pessoa_json)
    elif op == '2': #'2. Buscar cadastro'
        cpf = input('CPF: ')
        if os.path.exists (f'cadastros/{cpf}.json'):
            with open(f'cadastros/{cpf}.json', 'r') as f:
                pessoa_json = f.read()
                pessoa = json.loads(pessoa_json)
                print(f'Nome : {pessoa["nome"]} \nEmail: {pessoa["email"]} \nTelefone: {pessoa["telefone"]} \nCPF: {pessoa["cpf"]}')
        else:
            print('Pessoa não cadastrada!')
    elif op == '3': #'3. Listar cadastros'
        nome_arquivos = os.listdir('cadastros')
        tabela = []
        for nome_arquivo in nome_arquivos:
            with open(f'cadastros/{nome_arquivo}', 'r') as f:
                dados = json.load(f)
                linha = [
                    dados['nome'],
                    dados['email'],
                    dados['telefone']
                    dados['cpf']   
                ]
                tabela.append(linha)
        cabecalho = ['Nome', 'Email', 'Telefone', 'CPF']
        print(tabulate(tabela, headers=cabecalho, tablefmt='grid'))
                
    elif op == '4': #'4. Deletar cadastro'
        cpf = input('CPF: ')
        if os.path.exists (f'cadastros/{cpf}.json'):
            os.remove(f'cadastros/{cpf}.json')
            print('Cadastro deletado com sucesso!')
        else:
            print('Pessoa não cadastrada!')
    elif op == '5': #'5. Sair'
        break
    else: #ERRO
        print('Opção inválida. Tente novamente.')