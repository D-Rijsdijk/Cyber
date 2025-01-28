x = int(input('Insira um inteiro: '))
d = 2

while x < 1:
    print('X deve ser maior ou igual a 1.')
    x = int(input('Insira um inteiro: '))

while d < x :
    if x % d == 0:
        print(f'{x} não é primo')
        exit()
    d += 1
print(f'{x} é primo')