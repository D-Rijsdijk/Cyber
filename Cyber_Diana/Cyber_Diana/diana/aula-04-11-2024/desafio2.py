nota_um = float(input("Digite a nota da avaliação 1: "))
nota_dois = float(input("Digite a nota da avaliação 2: "))
nota_tres = float(input("Digite a nota da avaliação 3: "))

peso_um = float(input("Digite o peso da avaliação 1: "))
peso_dois = float(input("Digite o peso da avaliação 2: "))
peso_tres = float(input("Digite o peso da avaliação 3: "))

media = ((nota_um * peso_um) + (nota_dois * peso_dois) + (nota_tres * peso_tres)) / (peso_um + peso_dois + peso_tres)

if media < 5:
    print('Reprovado')
elif media >= 5 and media <= 7:
    print('Prova Final')
else:
    print('Aprovado')

