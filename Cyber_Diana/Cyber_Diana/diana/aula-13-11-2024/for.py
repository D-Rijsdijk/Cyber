x = int(input('Insira um inteiro: '))

while x < 1:
    print('X deve ser maior ou igual a 1.')
    x = int(input('Insira um inteiro: '))

for d in range(1, x + 1):
    r = x % d
    if r == 0:
        print(f'{d} é divisor de {x}')

"""
for y in range (10) -> y vai de 0 a 9
    print(y)
for y in range(1, 10) -> y vai de 1 a 9
    print(y)
for y in range (1, 11) - y vai de 1 a 10
    print(y)
"""