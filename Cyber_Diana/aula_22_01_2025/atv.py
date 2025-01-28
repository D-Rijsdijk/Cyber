''''
Faça um programa de cadastramento de pessoas. Neste programa o usuário deve informar o nome e o email de cada pessoa.
Uma lista deve ser formada com os cadastros, com a seguinte estrutura:

[('Fulano','fulano@mail.com'),
('Ciclano','ciclano@mail.com),
...]

No seu programa, deve haver uma opção de salvar e outro de carregar.
*Na opção de salvar, o programa salva a lista em um arquivo de texto.(Utilize a função str)
*Na opção carregar, o programa carrega a lista que está salva no arquivo de texto, e continua a operação com esta lista.
(Utilize a função eval)
'''
cadastros = []

while True:
    print('-----Menu-----')
    print('1. Cadastro de usuários')
    print('2. Listar cadastros')
    print('3. Salvar cadastros')
    print('4. Carregar cadastros')
    print('5. Encerrar programa')
    
    op = int(input('Escolha uma das opções. '))
    
    if op == 1:
        n = int(input('Quantos usuários você deseja cadastrar? '))
        for i in range(n):
            nome = input('Nome: ')
            email = input('Email: ') 
            cadastros.append((nome, email))
    elif op == 2:
        print('-----Lista de cadastros-----')
        for nome, email in cadastros:
            print(f'{nome}: {email}')
    elif op == 3:
        with open('cadastros.txt', 'w') as f:
            f.write(str(cadastros))
    elif op == 4:
        with open('cadastros.txt', 'r') as f:
            cadastros = eval(f.read())
    elif op == 5:
        break
    else:
        print('Opção inválida! Tente novamente.')