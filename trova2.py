







def taglia(lista,lista1):
    if len(lista1)!=0:
        
        if lista[0]!=lista1[0]:
            return taglia(lista[+1:],lista1[+1:])
        else:
            return  confronta(lista,lista1)

# # def controlla(lista,lista1):
#     if len(lista)!=0 and len(lista1)!=1:
#         if lista[0]!=lista1[1]:
#             return controlla(lista[+1:],lista1)
#         else:
#             return confronta(lista,lista1)



def confronta(lista,lista1,cont):
    
    
    
    if len(lista)!=0 and len(lista1)!=0:
        
            if lista[0] != lista1[0]:
                
                return taglia(lista,lista1)
            
            else:
                 return taglia(lista[+1:],lista1[+1:])
    
    if len(lista1)==0:
        return True
            
            
            
            
            # elif lista[0]==lista1[0] and cont==1:
            #     return confronta(lista[+1:],lista1[+1:],cont+1)
            # elif lista[0]==lista1[0] and cont==2:
            #     return confronta(lista[+1:],lista1[+1:],cont+1)
            # elif lista[0]==lista1[0] and cont==2:
            #     return confronta(lista[+1:],lista1[+1:],1)
            # 
            
            

            

lista=[]
lista1=[]
print("PRIMA LISTA ")
for x in range(int(input("Inserisci la lunghezza della lista "))):
    lista.append(int(input("Inserisci un numero ")))
    
print("SECONDA LISTA ")
for x in range(int(input("Inserisci la lunghezza della lista "))):
    lista1.append(int(input(" Inserisci un numero ")))

lista1.reverse()

# print(contanum(lista1))
if confronta(lista,lista1,0)==True:
    print("Trovato")
else:
    print("Non ho trovato")

