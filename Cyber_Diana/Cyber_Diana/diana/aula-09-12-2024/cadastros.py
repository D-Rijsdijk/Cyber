#Faça  um programa de cadastramento de pessoas com os seguintes requisitos: 
#1 - o programa mostra um menu de opções em loop. as opções são: 
    #a - cadastrar 
    #b - buscar 
    #c - remover 
#2 - na opção cadastrar, o usuário insere um cpf no formato xxx.xxx.xxx-xx , 
#um nome, um email, e uma data de nascimento no formato DIA/MES/ANO, e 
#estes dados são cadastrados. 
#3 na opção buscar, o usuario insere um cpf de um cadastro e o programa mostr os dados da pessoa com esse cpf 
#(nome, email e data de nascimento). 
#4 na opção remover, o usuario insere um cpf de um cadastro e o programadeleta o cadastro 
        #UTILIZE....


cadastros = dict() #para ser vazio. CRIAR UM DICIONARIO VAZIO 

while True: #FAZER UM LOOP COM MENU DE OPÇÃO
    print('1 - cadastrar')
    print('2 - buscar')
    print('3 - remover') 
    op = input('opções: ')
    if op == '1': #esse aqui é para cadastrar e precisão ser inseridos no cadastro do dicionário 
        #e tem que definir ele 
        cpf = input('CPF: ')
        nome = input('Nome: ')
        email = input('E-mail: ')
        nascimento = input('Nascimento') 
         #tem que adicionar os dados ao dicionário 
        cadastros[cpf] = (nome, email, nascimento)
    elif op == '2': #buscar, digita o cpf da pessoa e ele irá mostrar ele, buscar os dados atraves do cpf 
        cpf = input('CPF: ') 
        if cpf in cadastros.keys():
            dados = cadastros[cpf] #vai retornar e tem que ser atribuido a algum lugar, a uma variavel 
            nome_encontrado = dados[0]
            email_encontrado = dados[1]
            nascimento_encontrado = dados[2]
            print(nome_encontrado, email_encontrado, nascimento_encontrado)
        #OU 
        #nome_encontrado, email_encontrado, nascimento_encontrado = cadastro[cpf]
        #print(nome_encontrado, email_encontrado, nascimento_encontrado)
    elif op == '2':
        cpf = input('CPF: ')
        del cadastros[cpf] 
    else: 
        print('opção inválida')