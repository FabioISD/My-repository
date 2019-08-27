'''
from numpy import random
listaDeValores = random.rand(20)
for value in listaDeValores:
    print(value)

lista1 = ['q','w','e','r']
lista2 = ['i','u','y','t']
for v1,v2 in zip(lista1,lista2):
    print(v1,v2)

listaDeNomes = ['Pedro','João','Letícia']
for nome in listaDeNomes:
    print(nome)
else:
    print('Todos os nomes foram listados!')

#WHILE
contador = 0
while contador <=5:
    print(contador)
    decisao = int(input('O son-in tocou a barra?'))
    if(decisao):
        contador = contador + 1
print("Segue para a etapa 2 de treinamento!")

#WHILE/ELSE
decisao = True
while decisao:
    decisao = int(input('O son-in aprendeu a etapa 1?'))
    print(decisao)
else:
    print('O son-in não aprendeu a etapa 1')
'''
#Continue - interrompe um ciclo (continue e break)
count =-1
while count <5:
    count +=1
    if count ==3: continue
    print(count)
print('Fim do programa')