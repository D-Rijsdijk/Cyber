'''
Faça um programa de cadastramento de pessoas com os seguintes requisitos:

1 - O programa mostra um menu de opções em loop. As opções são:
    1 - Cadastrar
    2 - Buscar
    3 - Remover
    4 - Listar
2 - Na opção Cadastrar, o usuário insere um CPF no formato XXX.XXX.XXX-XX,
    um nome, um email e uma data de nascimento no formato DIA/MES/ANO, e
    estes dados são cadastrados.
3 - Na opção Buscar, o usuário insere um CPF de um cadastro e o programa
    mostra os dados da pessoa com esse CPF (nome, email e data de nascimento).
4 - Na opção Remover, o usuário insere um CPF de um cadastro e o programa
    deleta esse cadastro.
5 - Na opção Listar, o programa mostra uma lista com todos os cadastros.

Utilize um dicionário de tuplas para registrar os cadastros.
'''

cadastros = dict() # Cria um dicionário vazio

while True:
    print('1 - Cadastrar')
    print('2 - Buscar')
    print('3 - Remover')
    print('4 - Listar')
    op = input('Opção: ')

    if op == '1':
        cpf = input('CPF: ')
        nome = input('Nome: ')
        email = input('Email: ')
        nascimento = input('Nascimento: ')
        cadastros[cpf] = (nome, email, nascimento) # Insere um cadastro no dicionário
    elif op == '2':
        cpf = input('CPF: ')
        if cpf in cadastros.keys(): # Verifica se o CPF existe no dicionário
            # Busca os dados no dicionário associados ao CPF digitado
            nome_encontrado, email_encontrado, nascimento_encontrado = cadastros[cpf]
            print(nome_encontrado, email_encontrado, nascimento_encontrado)
        else:
            print('Cadastro não encontrado')
    elif op == '3':
        cpf = input('CPF: ')
        if cpf in cadastros.keys(): # Verifica se o CPF existe no dicionário
            del cadastros[cpf] # Remove o cadastro do dicionário
        else:
            print('Cadastro não encontrado')
    elif op == '4':
        print('\n------------------Lista de Cadastros------------------\n')
        print('CPF | NOME | EMAIL | NASCIMENTO')
        for cpf, dados in cadastros.items():
            (nome, email, nascimento) = dados
            print(f'{cpf}  | {nome}  |  {email}  |  {nascimento}')
    else:
        print('Opção inválida!')