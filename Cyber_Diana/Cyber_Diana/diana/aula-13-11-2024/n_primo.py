x = int(input('Insira um inteiro: '))
d = 1
count = 0

while x < 1:
    print('X deve ser maior ou igual a 1.')
    x = int(input('Insira um inteiro: '))

while d <= x :
    r = x % d
    if r == 0:
        count += 1
    d += 1
if count == 2:
    print(f'{x} é um número primo')
else:
    print(f'{x} não é número primo')
