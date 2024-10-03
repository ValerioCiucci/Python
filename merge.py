import random 

lista=[]


lista1=[]
lista2=[]
lista3=[]
listap=[]
listap.insert(0,lista)
listap.insert(1,lista1)
listap.insert(2,lista2)
listap.insert(3,lista3)

print(listap)

# while len(lista)>2:
#     lista1.append(lista[0])
#     lista.remove(lista[0])
# while len(lista1)>2:
#     lista2.append(lista1[0])
#     lista1.remove(lista1[0])
# while len(lista2)>2:
#     lista3.append(lista2[0])
#     lista2.remove(lista2[0])
for x in range(4):
    for y in range(2):
        
        listap[x].append(random.randint(0,20))
        

print(listap)

for x in range(4):
    if listap[x][0]>listap[x][1]:
        app=listap[x][0]
        listap[x][0]=listap[x][1]
        listap[x][1]=app
print(listap)

cont=0
for x in range(2):
    if listap[cont][0]>listap[cont+1][0]:
        app=listap[cont][0]
        listap[cont][0]=listap[cont+1][0]
        listap[cont+1][0]=app
    
    if listap[cont][1]>listap[cont+1][1]:
        app=listap[cont][1]
        listap[cont][1]=listap[cont+1][1]
        listap[cont+1][1]=app
    
    cont+=2
    
print(listap[0],listap[1],listap[2],listap[3])
    
    
    

# for x in range(4):
#     if x==0:
#         if lista[0]>lista[1]:
#             app=lista[0]
#             lista[0]=lista[1]
#             lista[1]=app
#     if x==1:
#         if lista1[0]>lista[1]:
#             app=lista1[x]
#             lista1[0]=lista1[1]
#             lista1[1]=app
#     if x==2:
#         if lista2[0]>lista2[1]:
#             app=lista2[0]
#             lista2[0]=lista2[1]
#             lista2[1]=app
#     if x==3:
#         if lista3[0]>lista3[1]:
#             app=lista3[0]
#             lista3[0]=lista3[1]
#             lista3[1]=app


        
    
    

# cont=1


# for x in range(len(lista)+len(lista)//3):
   
    
#     if cont==3:
#             lista.insert(x,"/")
#             cont=0
            



    

   