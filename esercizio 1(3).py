'''
num=int(input("Inserisci il numero di numeri da inserire "))
num2=[]

tot=0
for x in range(num):
    num2.insert(x,int(input("Inserisci il numero ")))
    if x==0:
        tot=num2[0]
    if tot>num2[x]:
        tot=num2[x]

print("il minore dei numeri inseriti e' ",tot)
''' 
for x in range(10):
    if x == 3:
        continue
    print(x)