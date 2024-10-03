

seme=input("Inserire il seme ")[0]
punteggio=input("Inserire il  punteggio ")
sseme=input("Inserire il seme ")[0]
spunteggio=input("Inserire il  punteggio ")


if punteggio=='k':
    punteggio=12

if punteggio=='q':
    punteggio=11

if punteggio=='j':
    punteggio=10

if seme=='c':
    seme=4
if seme=='q':
    seme=3
if seme=='f':
    seme=2
if seme=='p':
    seme=1

if spunteggio=='k':
    spunteggio=12

if spunteggio=='q':
    spunteggio=11

if spunteggio=='j':
    spunteggio=10

if sseme=='c':
    sseme=4
if sseme=='q':
    sseme=3
if sseme=='f':
    sseme=2
if sseme=='p':
    sseme=1



if int(punteggio)>int(spunteggio) :
    print("La prima carta ha piu valore ")
elif int(punteggio)<int(spunteggio) :
    print("La seconda carta ha piu valore ")
if int(punteggio)==int(spunteggio):
    if int(seme)>int(sseme):
            print("La prima carta ha piu valore ")
    else:
        print("La seconda carta ha piu valore ")

        




