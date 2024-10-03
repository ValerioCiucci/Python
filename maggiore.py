

lista=[]
colonne=int(input("Inserisci il numero di colonne da inserire nella tabella "))
for x in range(int(input("Inserisci il numero di righe da inserire nella tabella "))):
    lista.insert(x,[])
    print("NUOVA RIGA ",x)
    for y in range(colonne):
        
        lista[x].append(int(input("Inserisci un numero ")))

print(lista)

min=1000

for x in range(len(lista)):
    for y in range(colonne):
        
        if lista[x][y]<min:
            min=lista[x][y]
            app=x
            app1=y

print("il minore e' ",min,"in posizione x:",app,"y",app1)

for y in range(colonne):
    for x in range(len(lista)):
        
        if lista[x][y]<min:
            min=lista[x][y]
            app=x
            app1=y

print("il minore e' ",min,"in posizione x:",app,"y",app1)