def ordina(parola,parola1):
   
    if len(parola)!=0 and len(parola1)!=0:
        if parola[0]<parola1[0]:
            return parola[0]+ordina(parola.replace(parola[0],""),parola1.replace(parola1[0],""))
        else:
            return  parola1[0]+ordina(parola.replace(parola[0],""),parola1.replace(parola1[0],""))
        
            
    return ""
    
    




print(ordina(input("Inserisci una parola "),input("Inserisci un' altra parola ")))