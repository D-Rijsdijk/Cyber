#Modo 2

with open('emails.txt', 'r') as f:
    linhas = f.readlines()
 
 
for i in range(len(linhas)):
    linha_atual = linhas[i] #Obtém a i-ésima string da lista
    linha_atual = linha_atual.replace('\n', '') #Processa a string
    linhas[i] = linha_atual #Devolve a string processada para a mesma posição na lista

emails = [] #Lista que conterá apenas os emails
for linha in linhas:
    #Filtrar linhas para ignorar linhas em branco
    if linha != '':
        emails.append(linha)
        
print(linhas)