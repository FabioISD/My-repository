'''
from numpy import random
listaDeValores = random.rand(20)
for value in listaDeValores:
    print(value)

lista1 = ['q','w','e','r']
lista2 = ['i','u','y','t']
for v1,v2 in zip(lista1,lista2):
    print(v1,v2)
'''
listaDeNomes = ['Pedro','João','Letícia']
for nome in listaDeNomes:
    print(nome)
else:
    print('Todos os nomes foram listados!')
