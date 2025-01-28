while True:
    a = float(input('Insira o primeiro número: '))
    op = input('Escolha a operação que deseja realizar: ')
    b = float(input('Insira o segundo número: '))

    while op != '+' and op != '-' and op != '*' and op != '/':
        print("Operação inválida! Tente novamente.")
        op = input('Operador (+ , - , * ou /): ')
        
    if op == '/' and b == 0:
        print('Indefinição!')
        continue

    if op == '+':
        calc = a + b
        print(f'{a} {op} {b} = {calc}')
    elif op == '-':
        calc = a - b
        print(f'{a} {op} {b} = {calc}')
    elif op == '*':
        calc = a * b
        print(f'{a} {op} {b} = {calc}')
    else:
        calc = a / b
        print(f'{a} {op} {b} = {calc}')

    final = input('Digite "s" para sair ou qualquer outra tecla para continuar: ').lower()
    if final == 's':
        break
   