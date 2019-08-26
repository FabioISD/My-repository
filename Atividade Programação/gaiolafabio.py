hab = str(input('O animal está habituado? Sim or Não?')) 
if (hab=="Sim"):
    print('Iniciando protocolo') 
else:
    print('Você deve habituar o animal')

if hab == "Sim":
    aproximacao = float(input('Animal deve se aproximar da barra\n Simulando LEITURA DA DISTÂNCIA \n Digite a distância:' ))
    if (aproximacao<30):
        print('Aproximação necessária, liberando recompensa!\n')
    elif (aproximacao==30):
        print('Não houve aproximação necessária\n')
    else:
        print('Teste Cancelado')
if aproximacao:
    barra = int(input('Barra foi pressionada 20x?\n Ditige número de repetições: '))
    if (barra>=20):
        print('Animal passou para próxima Etapa\n') 
    else:
        print('Teste incompleto\n')
if barra >=20:
    print('BARRA deve ser pressionada de acordo com número do SOM.\n Para emitir Som Grave =1 , Som Agudo =2')
    som = int(input("Emitim o som"))
    barra = int(input("Pressionar barra"))
    if (som==1 and barra==1):
        print ("Liberar recompensa")
    elif (som==2 and barra==2):
        print ("Liberar recompensa")
    else:
        print("recompensa não liberada")

    

