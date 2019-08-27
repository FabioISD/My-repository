nome = str(input ('Qual seu nome?: '))
peso = float (input ('Qual seu peso(kg)?: '))
altura = float (input ('Qual sua altura(m)?: '))
imc = (peso/(altura*altura))
print ('Seu IMC é: {:.2f} e você está'.format(imc))
if (imc<17):
    print("muito abaixo do peso!")
elif (imc>17 and imc<18.5):
    print("abaixo do peso!")
elif (imc>18.5 and imc<25.0):
    print("com peso normal!")
elif (imc>25.0 and imc<30):
    print("acima do peso!")
else: 
    print("muito acima do peso!")