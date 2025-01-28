pessoas = {
    'fulano@mail.com': ('Fulano', '111.111.111-11'),
    'ciclano@mail.com': ('Ciclano','222.222.222-22'),
    'beltrano@mail.com': ('Beltrano','333.333.333-33')
}

print(pessoas)
email = input('Email: ')
dados = pessoas[email]
nome, cpf = dados
print(nome, cpf)

''' É possível fazer assim 
print(pessoas)
email = input('Email: ')
dados = pessoas[email]
cpf = dados
print(cpf)

'''