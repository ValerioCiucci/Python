giorno=int(input("Inserisci il giorno   "))
mese=int(input("Inserisci il mese   "))
anno=int(input("Inserisci l'anno    "))

if mese<13 and mese>0:
    if mese==1 or mese==3 or mese==5 or mese==7 or mese==8 or mese==10 or mese==12:
       
        if giorno<=31:
            print("La data inserita e' corretta")
        else:
            print("La data inserita non e' corretta")
            
            
            
    if  mese==4 or mese==6 or mese==9 or mese==11:
        
        if giorno<=30:
            print("La data inserita e' corretta")
        else:
            print("La data inserita non e' corretta")
            
    if mese==2  and anno%4==1:
        if giorno<=28:
            print("La data inserita e' corretta")
        else:
            print("La data inserita non e' corretta")
    if mese==2  and anno%4==0:
        if giorno<=29:
            print("La data inserita e' corretta")
        else:
            print("La data inserita non e' corretta")
else:
    print("Inserisci un mese valido")
        