def pegar_altura ():
    #Função que pede para o usuário digitar sua altura e retorna altura.
    altura = float(input('Informe sua altura (m): '))

    while altura <= 0: #Caso a altura seja inválida
        #Força o usuário a reescrever a altura
        print('Altura inválida! Tente novamente.')
        altura = float(input('Informe sua altura: '))
    return altura


def pegar_peso ():
        #Função que pede para o usuário digitar seu peso e retorna peso.
    peso = float(input('Informe seu peso (kg):'))

    while peso <= 0: #Caso o peso seja inválido
        #Força o usuário a reescrever o peso
        print('Peso inválido! Tente novamente.')
        peso = float(input('Informe seu peso:'))
    return peso


def calcular_imc(altura, peso):
    imc = peso / altura **2
    return imc


def classificar_imc(imc):
    if imc < 18.5:
        return 1 # Abaixo do peso
    elif imc < 25:
        return 2 # Peso normal
    else:
        return 3 #Acima do peso
    

    ### Código Principal ###

minha_altura = pegar_altura()
meu_peso = pegar_peso()
meu_imc = calcular_imc(minha_altura, meu_peso)
classificacao = classificar_imc(meu_imc)

if classificacao == 1:
    print('Abaixo do peso.')
elif classificacao == 2:
    print('Peso normal.')
elif classificacao == 3:
    print('Acima do peso.')
else:
    print('Classificação desconhecida.')