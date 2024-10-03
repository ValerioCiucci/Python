
num=int(input("Inserisci un numero "))
resto=0
stri=""
while num!=0:
    resto=str(num%2)
    num=num//2
    stri=stri+resto
for x in range(stri):
    

print(stri)
