'''
def mensagem_de_erro():
    """Função chamada sempre que houver um erro"""
    print("Erro!")
    print("Infelizmente você terá que fazer tudo novamente")
    print("Nada do que você fez está certo :´(")
mensagem_de_erro()

def soma(x,y):
    return x+y
primeiro_parametro = int(input("Ditige o primeiro número"))
segundo_paramento = int(input("Ditige o segundo número"))
y =  soma(primeiro_parametro,segundo_paramento)
print(y)

def arbitrary(x,y,*more):
    """Função com dois ou mais parâmetros"""
    print("x=",x,",y=",y)
    print("Parâmetros arbitrários: ",more)
arbitrary(2,3)
arbitrary(2,3,"oi","xau")

def nomes_paises(paises ="Noruega"):
    print("Eu vim da: ", paises)
nomes_paises("Venezuela")
nomes_paises()

def lista_de_comidas(comidas):
    """Programa para imprimir a lista de comidas passada"""
    for comida in comidas:
        print(comida)
lista_de_comidas(["Banana","Maça","Pera","Abacaxi"])

def recursao(k):
    if(k>0):
        resultado = k + recursao(k-1)
        print(resultado)
    else:
        resultado = 0
    return resultado
print(recursao(6))
'''
cube = lambda x: x*x*x
print(cube(7))