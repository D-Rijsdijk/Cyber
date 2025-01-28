"""
Faça um programa de banco de sangue com as seguintes características:
1 - O programa mostra um menu com as seguintes opções:
    1 - Cadastro doação
    2 - Obter doação
    3 - Listar doações
2 - Na opção 1, o usuário deve informar o tipo sanguíneo do doador, seu CPF e a data de doação.
3 - Na opção 2, o usuário deve informar o tipo sanguíneo, e deve obter a bolsa de sangue desse
tipo que está há mais tempo no banco.
4 - Na opção 3, o programa deve mostrar todas as bolsas presentes no banco para cada tipo sanguíneo.

Utilize um dicionário de listas.
As listas são compostas por tuplas.
"""
bolsas = {
    'A+': [],
    'A-': [],
    'B+': [],
    'B-': [],
    'O+': [],
    'O-': [],
    'AB+': [],
    'AB-': []
}

while True:
    print('1 - Cadastro de doações.')
    print('2 - Obter doações.')
    print('3- Listar doações')
    op = input('Opção: ')

    if op == '1':
        print('----------Cadastro de doações----------')
        tipo_sanguineo = input('Tipo sanguíneo:').upper()
        cpf = input('CPF: ')
        data = input('Data da doação: ')
        cadastro = (cpf, data)
        bolsas[tipo_sanguineo].append(cadastro)

    elif op == '2':
        print('----------Obter doações----------')
        tipo = input('Tipo sanguíneo requerido: ').upper()
        if len(bolsas[tipo]) > 0:
            cpf, data = bolsas[tipo].pop(0)
            print(f'A bolsa obtida foi doada no dia {data} pelo doador de CPF {cpf}')
        else:
            print('Não há bolsas disponíveis')
    elif op == '3':
        print('TIPO SANGUÍNEO | CPF DO DOADOR | DATA DA DOAÇÃO')
        for tipo, lista_bolsas in bolsas.items():
            for cpf, data in lista_bolsas:
                print(f'{tipo} | {cpf} | {data}')
    else:
        print('Opção inválida! Tente novamente.')