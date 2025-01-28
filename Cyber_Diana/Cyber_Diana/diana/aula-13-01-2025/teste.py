'''
Faça um programa para calcular as parcelas de um financiamento.
O usuário deve inserir:
- O valor a vista do bem (float)
- O valor da entrada (float)
- A taxa mensal de juros (float)
- A quantidade de parcelas (int)
O programa deve calcular e informar o valor das parcelas
'''
valor_a_vista = float(input('Valor a vista: '))
valor_de_entrada = float(input('Valor de entrada: '))
juros_mensal = float(input('Taxa mensal de juros: '))
parcelas = int(input('Quantidade de parcelas: '))

parcela = ((valor_a_vista - valor_de_entrada) * (1 + (juros_mensal/100))) / parcelas

print(f'Cada parcela terá o valor de {parcela:.2f}')