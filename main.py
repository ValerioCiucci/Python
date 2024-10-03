
end="no"
while end!="si":
    try:
    
        num=input('Inserisci un numero ')
        sim=input('Dammi il simbolo ')
        num2=input('Inserisci un numero ')

        if sim=="-":
            tot=int(num)-int(num2)
        elif sim=="+":
            tot=int(num)+int(num2)
        elif sim=="x":
            tot=int(num)*int(num2)
        elif sim=="/":
            tot=int(num)/int(num2)


        print("Ecco il risultato: " + str(tot))
        end=input("Vuoi terminare il programma? ")
    
    except:
        sim=input('Inserisci un simbolo valido ')
    if sim=="-":
        tot=int(num)-int(num2)
    elif sim=="+":
            tot=int(num)+int(num2)
    elif sim=="x":
            tot=int(num)*int(num2)
    elif sim=="/":
            tot=int(num)/int(num2)
    print("Ecco il risultato: " + str(tot))

 
 