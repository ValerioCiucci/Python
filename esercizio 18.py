ora=int(input("Inserisci l'ora "))
minuti=int(input("Inserisci i minuti "))
secondi =int(input("Inserisci i secondi "))

sora=int(input("Inserisci l'ora "))
sminuti=int(input("Inserisci i minuti "))
ssecondi =int(input("Inserisci i secondi "))

if ora<25 and ora>0 and ssora<25 and ssora>0 and minuti>0 and minuti<61 and ssminuti>0 and ssminuti<61  secondi>0 and secondi<61 and ssecondi>0 and ssecondi<61:

    if ora>sora:
        print(" il primo orario e' maggiore del secondo ")
    elif ora<sora:
        print("Il secondo orario e' maggiore del secondo ")

    if ora==sora:
    
        if minuti>sminuti:
         print("Il primo orario è maggiore del secondo ")
        elif minuti<sminuti:
         print("Il secondo orario è maggiore del secondo")
        else:
            if secondi>ssecondi:
                print("Il primo orario è maggiore del secondo ")
            else:
                print("Il secondo orario è maggiore del secondo ")
                if secondi==ssecondi:
                    print("gli orari sono uguali")
    
        
