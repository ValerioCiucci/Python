
# def confronta(lista,lista1):
#     if len(lista)!=0 and len(lista1)!=0:
#         if lista[0]==lista1[0]:
            
#             return lista1[0]+confronta (lista.remove(lista[0]),lista1.remove(lista[0]))
        
#     return ""


        
# def rimuovi(lista):
#     lista.remove(lista[0])
#     return lista

# def contanum(lista):
#     lista2=[]
#     if lista[0]==lista[1] and lista[0]!= lista[1] and lista[0]!= lista[2]:
#         lista2.append(2)
#         lista2.append(lista[0])
#         return lista2
#     elif lista[0]==lista[2] and lista[0]!= lista[1]:
#         lista2.append(2)
#         lista2.append(lista[0])
#         return lista2
#     elif lista[0]==lista[1] and lista[0] == lista[2]:
#         lista2.append(3)
#         lista2.append(lista[0])
#         return lista2
#     elif lista[1]==lista[2]:
#         lista2.append(2)
#         lista2.append(lista[1])
#         return lista2
    
#     if lista2==[]:
#         lista2.append(0)
#         return lista2

    
#     return lista2

def confronta(lista,lista1,cont):
    
    if cont==len(lista1) and cont!=0:
            return True
    
    if len(lista)!=0:
        
            if lista[0] == lista1[0] and cont==0:
                return confronta(lista[+1:],lista1,cont+1)

            elif lista[0]==lista1[1] and cont==1:
                return confronta(lista[+1:],lista1,cont+1)
            elif lista[0]==lista1[2] and cont==2:
                return confronta(lista[+1:],lista1,cont+1)
            elif lista[0]==lista1[0] and cont==2:
                return confronta(lista[+1:],lista1,1)
            else:
                return confronta(lista[+1:],lista1,0)
            
        # if contanum(lista1)[0]>0:
        #     if lista[0] == lista1[0] and cont==0:
                
        #         return confronta(lista[+1:],lista1,cont+1)
        #     elif lista[0]==lista1[1] and cont==1:
        #         return confronta(lista[+1:],lista1,cont+1)
            
        #     elif lista[0]==lista1[2] and cont==2:
        #         return confronta(lista[+1:],lista1,cont+1)
            
        #     else:
        #         return confronta(lista[+1:],lista1,0)
        # elif cont==len(lista1):
        #     return True
            

lista=[]
lista1=[]
print("PRIMA LISTA ")
for x in range(5):
    lista.append(int(input("Inserisci un numero ")))
    
print("SECONDA LISTA ")
for x in range(3):
    lista1.append(int(input(" Inserisci un numero ")))

lista1.reverse()

# print(contanum(lista1))
if confronta(lista,lista1,0)==True:
    print("Trovato")
else:
    print("Non ho trovato")

