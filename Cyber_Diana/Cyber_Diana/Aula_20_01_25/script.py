"""
arquivo = open('meutexto.txt','r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)
"""
'''
with open('meutexto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    
print(conteudo)
'''

with open('../arquivo/meutexto.txt', 'w') as arquivo:
    arquivo.write('Meu nome nao e Filipe')
    arquivo.write(' Meu nome e Diana')
    