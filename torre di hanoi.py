
def risolvi(n,pos,cont):
    
    if cont%2==1:
        print("sposta disco n ",cont,"verso ",pos)
        
        cont+=1
        
        
        
        
    if cont%2==0:
        pos+=1
        print("sposta disco n ",cont,"verso ",pos)
        

        
    
        
        
    return risolvi(n,pos)


numero=int(input("Inserisci il numero di dischi da inserire nella torre "))
risolvi(numero,3,1)

