x=int(input("Inserisci un numero "))
y=int(input("Inserisci un numero "))

for i in range(x):
    if x%(i+1)==0:
        if (i+1)<y and (i+1)>0:
            print(i+1)