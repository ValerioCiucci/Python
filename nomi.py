
import random

nome=input("Inserisci il nome che vuoi cercare ")
intervallo=int(input("Inserisci il nome di numeri da inserire "))
lista=[]

stringa=""


for x in range(int(intervallo)):
    for x in range(random.randint(1,10)):
        stringa=stringa+chr(random.randint(97,122))
    lista.insert(len(lista),stringa)
    stringa=""

y=0
print (lista)
app=""
for x in range(len(lista)):
    y+=1
    for y in range (len(lista)):
        
        if ord(lista[x][0])<ord(lista[y][0]):
            app=lista[y]
            lista[y]=lista[x]
            lista[x]=app
print (lista)
flag=False
app=int(intervallo/2)
app1=int((intervallo-1+app)/2)

while flag!=True:
    
    if lista[app][0]==nome:
        print(app,"trovato")
        break
    if ord(lista[app][0])<ord(nome) and app<app1:
        app+=1
        if lista[app][0]==nome:
            print(app,"trovato")
            break
    elif app1-app==1 or app1-app==0:
        app=app1
        app1=intervallo
        
    if ord(lista[app][0])>ord(nome) and app<app1:
        s=+1
        if s==1:
            app1=app
            app=0
        else:
            app+=1
        if app!=0:
            app1=2
        else:
            app1=int((app1+app)/2)
        if lista[app]==nome:
            print(app,"trovato")
            break
    elif app1-app==1 or app1-app==0:
        app=app1
        app1=int(intervallo/2)
    else:
        print("Il valore inserito non è stato trovato ")
        break