'''
Faça um código que transforme a minha_lista em uma lista com nomes em caixa alta.
Utilize for e o método upper de string 
'''
minha_lista = ['Fulano', 'Ciclano', 'Beltrano']
print('Antes: ', minha_lista)

#minha_lista = [i.upper() for i in minha_lista]
for i in range(len(minha_lista)):
    string_atual = minha_lista[i]
    string_caixa_alta = string_atual.upper()
    minha_lista[i] = string_caixa_alta

print('Depois: ', minha_lista)