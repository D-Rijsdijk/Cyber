while True:
    x = int(input('Insira um número inteiro:'))
    if x % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
    op = input('Digite "s" para sair ou qualquer outra tecla para continuar: ')
    if op == 's':
        break
print('Até mais!')