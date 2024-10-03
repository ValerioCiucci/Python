voto=int(input("Inserisci il voto "))
if voto>0 and voto<=10:
    if voto>5:
        print("Il voto e' sufficiente ")
    elif voto==5:
        print("Il voto è insufficiente")
    else:
        print("Il voto è gravemente insufficiente")
else:
        print("Inserisci una votazione valida")

    
