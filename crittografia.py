
def crittografa(frase,chiave,chiave1,cont):
    if len(frase)!=0:
        if cont%2==0:
            if ord(frase[0])+chiave>=122:
                
                
                frase=frase.replace(frase[0],chr(ord(frase[0])+chiave-122))

                
            return chr(ord(frase[0])+chiave) + crittografa(frase[+1 :],chiave,chiave1,cont+1)
        
        else:
             if ord(frase[0])+chiave>=122:
                    frase=frase.replace(frase[0],chr(ord(frase[0])+chiave-122))

             return chr(ord(frase[0])+chiave1) + crittografa(frase[+1 :],chiave,chiave1,cont+1)

    return ""

def decrittografa(frase,chiave,chiave1,cont):
    if len(frase)!=0 :
        if cont%2==0:
            if ord(frase[0])+chiave>=122:
                
                
                frase=frase.replace(frase[0],chr(97))
                chiave=ord(frase[0])+chiave-122
                
            
            return chr(ord(frase[0])-chiave) + decrittografa(frase[+1 :],chiave,chiave1,cont+1)
        else:
            if ord(frase[0])+chiave>=122:
                
                frase=frase.replace(frase[0],chr(ord(frase[0])+chiave-122))

            
            return  chr(ord(frase[0])-chiave1) + decrittografa(frase[+1 :],chiave,chiave1,cont+1)

    return ""

chiave=int(input("Inserisci una chiave "))
chiave1=int(input("Inserisci un' altra chiave "))
frase=input("Inserisci una frase ")
frase=crittografa(frase, chiave,chiave1 ,0)
print("parola criptata: ",frase)

print("parola decriptata: ",decrittografa(frase, chiave,chiave1,0))

