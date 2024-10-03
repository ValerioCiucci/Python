
def controlla(frase,lettera):
    cont=0
    for x in range(len(frase)):
        if frase[x]==lettera:
            cont+=1
    
    return cont
        
    

frase=input("INSERISCI LA FRASE ")
lettera=input("INSERISCI QUALE LETTERA CONTROLLARE ")
print(controlla(frase,lettera)) 