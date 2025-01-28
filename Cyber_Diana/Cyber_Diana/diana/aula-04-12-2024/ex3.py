pessoas = {
    'fulano@mail.com': ('Fulano', '111.111.111-11'),
    'ciclano@mail.com': ('Ciclano','222.222.222-22'),
    'beltrano@mail.com': ('Beltrano','333.333.333-33')
}

print(pessoas)

email = input('Email para inserir: ')
nome = input('Nome para inserir: ')
pessoas[email] = nome #Inserir chave no dicionário

email2 = input('Email para remover: ')
del pessoas[email2] #Remover do dicionário


print(pessoas)
