a=int(input("Inserisci il valore del primo lato "))
b=int(input("Inserisci il valore del secondo lato "))
c=int(input("Inserisci il valore del terzo lato "))

if a*a+b*b==c*c:
    print("Questo triangolo è rettangolo")
if c*c+b*b==a*a:
    print("Questo triangolo è rettangolo")
if a*a+c*c==b*b:
    print("Questo triangolo è rettangolo")
