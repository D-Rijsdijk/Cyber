'''
Faça um programa em que o usuário insere uma rota de viagem passando pelas seguintes cidades do MT:

 # índice - cidade
 #  0 - 'Cuiabá'
 #  1 - 'Rondonópolis'
 #  2 - 'Primavera do Leste'

 Você deve completar o código para que o programa mostre o tempo total de uma viagem passando por pelo menos 2 cidades.

 Exemplos de rota: 0,1,2,0
                    0,2,1,0
                    1,0,2,0,1
 '''

def obter_rota():
    qtd_pontos = int(input('Quantos pontos de parada deseja inserir?'))
    while qtd_pontos < 2:
        print('A rota deve ter no mínimo 2 pontos')
        qtd_pontos = int(input('Quantos pontos de parada deseja inserir?'))
    rota = []
    for i in range(qtd_pontos):
        cidade = int(input(f'Insira a {i+1} cidade (0, 1, 2):'))
        rota.append(cidade)
    return rota


tempo_de_viagem = (
    (0,3.25,3.5),
    (3,0,3.1),
    (3.5,2,0)
) # distancia[origem][destino]

rota = obter_rota()
print(rota)

tempo_total = 0
for i in range(len(rota)-1):
    origem = rota[i]
    destino = rota[i+1]
    tempo = tempo_de_viagem[origem][destino]
    tempo_total += tempo

print(f'Tempo total da viagem: {tempo_total} horas')
