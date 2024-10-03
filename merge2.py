import random

def merge(lista):
    
    if len(lista)<=1:
        return lista
    else:
        meta1=lista[0:len(lista)//2]
        meta2=lista[len(lista)//2:]
        
    merge(meta1)
    merge(meta2)
    
    lista=sort(meta1,meta2)
    
        


def sort(lista,lista1):
    lista2=[]
    x=0
    y=0
    
    while len(lista2)<=len(lista)+len(lista1):
     if lista[x]<lista1[y]:
         lista2.append(lista[x])
         lista2.append(lista1[y])
    x+=1
    y+=1
    
    return lista2
   



lista=[]

numeri=int(input("Inserisci il numero di numeri da inserire "))
for x in range(numeri):
    lista.append(random.randint(0,100))
print(lista)
print(merge(lista))