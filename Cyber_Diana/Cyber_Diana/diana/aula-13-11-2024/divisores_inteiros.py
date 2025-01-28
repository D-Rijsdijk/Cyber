x = int(input('Insira um inteiro: '))
d = 1

while x < 1:
    print('X deve ser maior ou igual a 1.')
    x = int(input('Insira um inteiro: '))

while d <= x :
    r = x % d
    if r == 0:
        print(f'{d} é divisor de {x}')
    d += 1
