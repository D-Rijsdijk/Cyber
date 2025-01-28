capital = float(input('Capital investido (R$): '))
taxa = float(input('Taxa de rendimento anual (%): '))
tempo = float(input('Tempo de aplicação (anos): '))
montante = capital * (1 + taxa/100)** tempo
rendimento = montante - capital

print(f'O rendimento é de R${rendimento:.2f}')
print(f'O montante é de R${montante:.2f}')