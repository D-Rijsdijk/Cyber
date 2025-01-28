a = float(input('Digite o valor do coeficiente a: '))
b = float(input('Digite o valor do coeficiente b: '))
c = float(input('Digite o valor do coeficiente c: '))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('Nenhuma solução real.')
elif delta > 0:
    print('Duas soluções reais.')
else:
    print('Uma solução real')