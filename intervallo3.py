


import random



            
    
    
    
    
    
    
    
    
    
    
    
def cerca(lista,imin,imax,numero,app):
   
    
   
    
    media=(imax+imin)//2
    
    if app==media:
        return False
    
    if lista[media]==numero:
       
        return media
        
        
    
    elif lista[media]>numero:
        
        imax=media
        
    elif lista[media]<numero:
        imin=media
    
    app=media
    
    return cerca(lista,imin,imax,numero,app)

def ordina(lista,cont,y):
    
    
    
    
    
    if cont<len(lista):
        
        y=0
        return ordinay(lista,cont,y)
        
    
    if len(lista)==cont:
        
        return lista
    
 
    
    return ordina(lista,cont,y)
    
def ordinay(lista,cont,y):
    
 
    
    if y<len(lista):
            
            if lista[cont]<lista[y]:
                    appo=lista[y]
                    lista[y]=lista[cont]
                    lista[cont]=appo
    
    y+=1
    if y==len(lista):
        cont+=1
        return ordina(lista,cont,y)
    return ordinay(lista,cont,y)
   


numero=int(input("Inserisci il numero che vuoi cercare "))
intervallo=int(input("Inserisci il numero di numeri da inserire "))
lista=[]

for x in range(int(intervallo)):
    lista.insert(len(lista),random.randint(0,10))
print (lista)
# y=0
# for x in range(len(lista)):

#     for y in range (len(lista)):
        
#         if lista[x]<lista[y]:
#             app=lista[y]
#             lista[y]=lista[x]
#             lista[x]=app
print(ordina(lista,1,0))
imax=intervallo-1

if(cerca(lista,0,imax,numero,0))==False:
    print("Numero non trovato ")
else:
    print(cerca(lista,0,imax,numero,0), "trovato ")