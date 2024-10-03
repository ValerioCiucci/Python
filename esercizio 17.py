a=int(input("Inserisci il primo valore "))
b=int(input("Inserisci il primo valore "))
c=int(input("Inserisci il primo valore "))


if a>b and a>c or b>c and a==b or c>b and c==a:
    print("Il primo valore è maggiore ")
if b>a and b>c or   a>c and b==a or c>a and b==c :
    print("Il secondo valore è maggiore ")
if c>b and c>a or a>b   and c==a or b>a  and c==b :
    print("Il terzo valore è maggiore ")
