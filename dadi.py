import random

#2 o 12 perdi  primo lancio 
#prima volta 7 vinci
 # altri lanci 7 perdi e se fai il numero precedente hai vinto

fine=False
tot=0
turno=0 
while fine!=True:

    dado=random.randint(1,6)
    dado1=random.randint(1,6)
    print("turno ",turno)
    print("PRIMO LANCIO ",dado,"SECONDO LANCIO", dado1)
    print("TOTALE: ", dado+dado1)
    if turno>0:
        if dado+dado1==7:
            print("HAI PERSO ")
            fine=True
            break
        if dado+dado1==tot:
            print("HAI VINTO ")
            fine=True
            break
    if dado+dado1==12 or dado+dado1==2 and turno==0:
        print("HAI PERSO ")
        fine=True
        break
    if dado+dado1==7 and turno==0:
        print("HAI VINTO ")
        fine=True
        break
    if turno==0:
        tot=dado+dado1
        print("TOTALE DA RAGGIUNGERE: ",tot)
    turno+=1
    