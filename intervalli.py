
import random




numero=int(input("Inserisci il numero che vuoi cercare "))
intervallo=int(input("Inserisci il numero di numeri da inserire "))
lista=[]

for x in range(int(intervallo)):
    lista.insert(len(lista),random.randint(0,10))
print (lista)
y=0
for x in range(len(lista)):
    y+=1
    for y in range (len(lista)):
        
        if lista[x]<lista[y]:
            app=lista[y]
            lista[y]=lista[x]
            lista[x]=app
s=0
print (lista)
flag=False
app=int(intervallo/2)
app1=int((intervallo-1+app)/2)
while flag!=True:
    
    if lista[app]==numero:
        print(app,"trovato")
        break
    if lista[app]<numero and app<app1:
        app+=1
        if lista[app]==numero:
            print(app,"trovato")
            break
    elif app1-app==1 or app1-app==0:
        app=app1
        app1=intervallo
        
    if lista[app]>numero and app<app1:
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
        if lista[app]==numero:
            print(app,"trovato")
            break
    elif app1-app==1 or app1-app==0:
        app=app1
        app1=int(intervallo/2)
    else:
        print("Il valore inserito non è stato trovato ")
        break