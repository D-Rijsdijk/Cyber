'''
Faça um código que transforma a minha_lista em uma lista com nomes em caixa alta e em ordem alfabética.
Utilize for, o método upper de string e sort.
'''
minha_lista = ['Fulano', 'Ciclano', 'Beltrano']
print('Antes: ', minha_lista)

#minha_lista = [i.upper() for i in minha_lista]
for i in range(len(minha_lista)):
    string_atual = minha_lista[i]
    string_caixa_alta = string_atual.upper()
    minha_lista[i] = string_caixa_alta

minha_lista.sort()
print('Depois: ', minha_lista)