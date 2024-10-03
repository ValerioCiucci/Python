b=int(input("Inserisci la base "))
h=int(input("Inserisci l'altezza "))
sim='x'

for x in range(h):
    for x in range(b):
        if x==0:
            sim='*'
        else:
            sim=sim+'*'
    
    print(sim)
    sim='x'


    