
tot=0
conti=0
for x in range(10):
    numv=int(input("Inserisci il numero dei voti "))
    for x in range(numv):
        voto=int(input("Inserisci il voto dell'alunno "))
        if voto<6:
            conti+=1
            
            
        tot=tot+voto
        
    media=tot/numv
    print("Media alunno:",media )
    print("L'alunno ha ",conti," insufficienze ")
    conti=0
    media=0
    tot=0
    numv=0
    