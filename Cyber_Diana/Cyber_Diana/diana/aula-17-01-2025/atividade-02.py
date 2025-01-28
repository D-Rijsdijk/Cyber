despesas = dict()

renda_mensal = float(input('Informe sua renda mensal (R$): '))

while True:
    despesa = input('Informe o nome da sua despesa: ')
    gasto = float(input('Informe o valor da sua despesa (R$): '))
    despesas[despesa] = gasto
    
    saida = input('Deseja informar outra despesa? (s/n)').lower()
    
    if saida == 'n': # Lembrando que o s é afirmando que deseja informar outra despesa e não que deseja prosseguir
        break
    
valores = [gasto for despesa, gasto in despesas.items()]
gastos = sum(valores) #Gasto total do mês

lucro_mensal = renda_mensal - gastos #Quanto dinheiro sobra (ou falta) por mês



