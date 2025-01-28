a_vista = float(input('Informe o valor do bem a vista (R$):'))
valor_de_entrada = float(input('Informe o valor de entrada (R$): '))
juros_mensal = float(input('Informe a taxa mensal de juros (%): '))
parcelas = int(input('Informe a quantidade de parcelas: '))

parcela = (a_vista - valor_de_entrada) * (((1 + (juros_mensal/100)) ** parcelas) * (juros_mensal/100)) / (((1 + (juros_mensal/100)) ** parcelas) - 1)

print(f'Cada parcela terá o valor de {parcela:.2f}')