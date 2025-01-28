'''
Dicionários:
* É uma coleção de dados associativa.
* No dicionário não existe uma ordem para os dados (1,2,3,4, etc) e cada dado é associado a uma chave
# A chave deve ser única de cada valor
'''
pessoas = {
    'fulano@mail.com': 'Fulano',
    'ciclano@mail.com': 'Ciclano',
    'beltrano@mail.com': 'Beltrano'
}

email = input('Email: ')
nome = pessoas[email] #encontrar o nome do email que o usuário digitou 
print(nome)