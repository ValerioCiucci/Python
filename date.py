from datetime import date

def converti(mese):
    tot=0
    
    for x  in range(mese+1):
        if x==3 or x==5 or x==7 or x==8 or x==10 or x==12 and mese+1!=x:
            tot=tot+31
        elif x==4 or x==6 or x==9 or x==11 and mese+1!=x:
            tot=tot+30
        elif x==2 and mese+1!=x:
            tot=tot+28
    return tot


data=date.today()


mese=data.month
giorno=data.day
anno=data.year

gNascita=int(input("Inserisci il giorno della tua nascita   "))
mNascita=int(input("Inserisci il mese della tua nascita "))
aNascita=int(input("Inserisci l' anno della tua nascita "))

diff=0
totg=0
totg=converti(mNascita)+gNascita
totg1=converti(mese)+giorno

if totg<totg1:
    diff=totg-totg1+365
elif totg>totg1:
    diff=totg-totg1
else:
    diff=365
    
print("Mancano esattamente ",diff, "giorni al tuo compleanno!")

    