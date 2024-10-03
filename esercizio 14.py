a=int(input("Inserisci il valore di a  "))
b=int(input("Inserisci il valore di b "))
c=int(input("Inserisci il valore di c "))

delta=b*b-4*a*c
if delta<0:
    print("Questa equazione non ha soluzioni")
elif delta==0:
    tot=-b+sqrt(delta)/2*a
    print("Ecco il risultato dell'equazione: "+ str(tot))
        

else: 
    tot1=-b+sqrt(delta)/2*a
    tot2=-b-sqrt(delta)/2*a
    print("Ecco i risultati dell'equazione: "+ str(tot1)+ " - "+ str(tot2))
