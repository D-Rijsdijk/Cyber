'''
Faça um programa em python que escreva uma lista de emails inseridos 
pelo usuario em um arquivo, nos seguintes formatos:

fulano@mail.com
ciclano@mail.com
beltrano@mail.com
'''
emails = []

while True:
    email = input('Email: ')
    emails.append(email)
    
    continuar = input('Deseja inserir mais algum email (s/n)? ').lower()
    if continuar == 'n':
        break
    
with open('meutexto.txt', 'w') as arquivo:
    for email in emails:
        arquivo.write(email + '\n')