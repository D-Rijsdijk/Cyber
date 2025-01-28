def teste (num):
    if num % 2 == 0:
        return True
    else:
        return False

variavel = int(input('Digite um número inteiro: '))

if teste(variavel):
    print('O número é par!')
else:
    print('O número é ímpar!')
