'''
DESAFIO:
Faça um programa de cadastramento que:
1- Mostra, em loop, um menu com as opções:
    1.1 - Cadastrar
    1.2 - Lista cadastros
    1.3 - Buscar cadastro
2 - Na opção 'cadastrar', o usuário insere os dados da pessoa, sendo eles:
nome, email, cpf e data de nascimento. Em seguida, a pessoa é cadastrada no sistema.
3 - Na opção 'listar cadastros', uma tabela com os dados de todos os cadastros é mostrada no terminal.
4 - Na opção 'buscar cadastro', o usuário insere um nome e o programa mostra uma tabela com os dados
de todas as pessoas com esse nome.

    Utilize uma lista de tuplas para armazenar os cadastros. Cada cadastro deve ser armazenado na lista com uma tupla.
'''
#Nome | Email | CPF
#Fulano | fulano@email.com| 666.666.666-66

if __name__ == '__main__':
    lista_de_cadastro = []

    while True:
        print('\n---MENU---\n')
        print('1 - Cadastrar')
        print('2 - Lista cadastros')
        print('3 - Buscar cadastros')
        op = int(input('\n Selecione uma das opções!\n'))

        if op == 1:
            nome = input('Nome: ')
            email = input('Email: ')
            cpf = input('CPF: ')
            data_nascimento = input('Data de nascimento: ')
            cadastro = (nome, email, cpf, data_nascimento)
            lista_de_cadastro.append(cadastro)

        elif op == 2:
            print('\n---------------------------Cadastros Realizados---------------------------\n')
            print("Nome | Email | CPF | Data de Nascimento")
            print('----------------------------------------------------------------------------')
            for nome, email, cpf, data_nascimento in lista_de_cadastro:
                print(f'{nome} |{email} |{cpf} |{data_nascimento}')

        elif op == 3:
            buscar_cadastro = input('Nome: ')
            print('\n---------------------------Cadastros Realizados---------------------------\n')
            print("Nome | Email | CPF | Data de Nascimento")
            print('----------------------------------------------------------------------------')
            for nome, email, cpf, data_nascimento in lista_de_cadastro:
                if nome == buscar_cadastro:
                    print(f'{nome} |{email} |{cpf} |{data_nascimento}')

        else:
            print('A opção selecionada não existe!')

                