intervallo=int(input("Inserisci il numero di numeri da inserire "))
num=[]
flag=False
for x in range(intervallo):
    numi=int(input("Inserisci il numero "))
    num.insert(len(num),numi)
    if numi==0 and flag==False:
        pos=x
        flag=True
    if numi==1:
        pos1=x
print(num)
app=num[pos1]
num[pos1]=num[pos]
num[pos]=app
print(num)