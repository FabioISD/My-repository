'''
#Função range repetição de contagem de valores
for i in range(10): 
    print(i)

for i in range(9,-1,-3): 
    print(i)

# Função range repetição de contagem de caractere
for char in "Fábio Medeiros":
    print(char)

# Função para contagem de lista
listaDeNomes = ['Pedro','João','Letícia']
for nome in listaDeNomes:
    print(nome)

#Funções Range/Lista
linguagens = ['Python','C++','C','Raskel','Gobol']
tamanho = len(linguagens) #retorna o tamanho da lista
indices = range(tamanho) #retorna os indices que serão utilizados para acessar a lista
for i in indices:
    print(linguagens[i])

#Função enumerate (Númera os elementos da lista)
for key,value in enumerate(['p','y','t','h','o','n']):
    print(key, value)
#Windowns (C:\Users\fabio.bezerra\AppData\Local\Programs\Python\Python37-32\python.exe -m pip install numpy)
#Linux (python -m pip install numpy) / /usr/bin/python3.7 -m pip install numpy
linguagens = ['Python','C++','C','Raskel','Gobol']
for key,value in enumerate(linguagens):
    print('A linguagem é: ', value)
    print('O rank da linguagem é: ',key)
'''

from numpy import random
listaDeValores = random.rand(20)
for value in listaDeValores:
    print(value)