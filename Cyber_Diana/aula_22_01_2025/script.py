#Modo 01

with open('emails.txt', 'r') as f:
    conteudo = f.read()    

#emails = conteudo.split('\n')

#print(emails)

emails = []
for linha in conteudo.split('\n'):
    if linha != '':
        emails.append(linha)
        
print(emails)