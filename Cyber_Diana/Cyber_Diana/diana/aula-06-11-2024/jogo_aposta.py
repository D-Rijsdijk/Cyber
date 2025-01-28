from random import randint

aposta1 = int(input('Aposte em seu primeiro número de 0 a 9: '))

if aposta1 < 0 or aposta1 > 9:
    print('Aposta 1 inválida!')
    exit()

aposta2 = int(input('Aposte em seu segundo número de 0 a 9: '))

if aposta2 < 0 or aposta2 > 9:
    print('Aposta 2 inválida!')
    exit()

num1 = randint(0, 9)
num2 = randint(0, 9)
num3 = randint(0, 9)
num4 = randint(0, 9)

print(num1, num2, num3, num4)

premio = 0
if aposta1 == num1 or aposta1 == num2 or aposta1 == num3 or aposta1 == num4:
    premio += 1000
if aposta2 == num1 or aposta2 == num2 or aposta2 == num3 or aposta2 == num4:
    premio(f'O prêmio é de R${premio}')