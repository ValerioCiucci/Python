def somma(num,num2):
    return int(num)+int(num2)
def sottrazione(num,num2):
    tot=int(num)-int(num2)
    return tot
def moltiplicazione(num,num2):
    tot=int(num)*int(num2)
    return tot
def divisione(num,num2):
    tot=int(num)/int(num2)
    return tot
def calcolo(s,num,a):
    for x in range(len(num)-1):
        if s[a[x]]=='+': 
            tot=somma(num[0],num[1])
            num.remove(num[0])
            num.remove(num[0])
            num.insert(0,tot)
            print(num)
            print(x)
        if s[a[x]]=='-':
            tot=sottrazione(num[0],num[1])
            num.remove(num[0])
            num.remove(num[0])
            num.insert(0,tot)
            print(num)
            print(x)
        if s[a[x]]=='*':
            tot=moltiplicazione(num[0],num[1])
            num.remove(num[0])
            num.remove(num[0])
            num.insert(0,tot)
            print(num,"numero")
        if s[a[x]]=='/':
            if flag1==True:
                l2=num[1]
                num.remove(num[1])
                num.insert(0,l2)
            tot=divisione(num[0],num[1])
            num.remove(num[0])
            num.remove(num[0])
            num.insert(0,tot)
    print(len(num))
    return num
s=input("Inserisci l'operazione da svolgere ")
num=[]
l=""
tot=0
pr=0
flag=False
flag1=False
a=[]
par=[]
aP=[]
P=False
for x in range(len(s)):
    if s[x]=='0' or s[x]=='1' or s[x]=='2' or s[x]=='3' or s[x]=='4' or s[x]=='5' or s[x]=='6' or s[x]=='7' or s[x]=='8' or s[x]=='9':
        l=l+s[x]
    elif s[x]=='*':
        if P==False: 
            if pr==2:
                flag1=True
            num.insert(0,l)
        else:
            if pr==2:
                flag1=True
            par.insert(0,l)
        l=""
        flag=True
        pr=3
        if P==False:
            a.insert(0,x)
        else:
            aP.insert(0,x)
    elif s[x]=='+':
        if P==False:
            if pr==3:
                num.insert(1,l)
            elif pr==2:
                num.insert(1,l)
            else:
                num.insert(len(num),l)
        else:
            if pr==3:
                par.insert(1,l)
            elif pr==2:
                par.insert(1,l)
            else:
                par.insert(len(num),l)
        l=""
        pr=1
        if P==False:
            a.insert(len(a),x)
        else:
            aP.insert(len(aP),x)
    elif s[x]=='-':
        if P==False:
            if pr==3:
                num.insert(1,l)
            elif pr==2:
                num.insert(1,l)
            else:
                num.insert(len(num),l)
        else:
             if pr==3:
                par.insert(1,l)
             elif pr==2:
                par.insert(1,l)
             else:
                par.insert(len(num),l)   
        pr=1
        l=""
        if P==False:
            a.insert(len(a),x)
        if P==True:
            aP.insert(len(aP),x)
    elif s[x]=='/':
        if P==False:
            if pr==3:
                num.insert(1,l)
                a.insert(1,x)
            else:
                num.insert(0,l)
                a.insert(0,x)
        else:
            if pr==3:
                par.insert(1,l)
                aP.insert(1,x)
            else:
                par.insert(0,l)
                aP.insert(0,x)
        pr=2
        l=""
    elif s[x]=='(':
        P=True
    elif s[x]==')':
        print(l, "l ")
        par.insert(len(par),l)
       
      
        num.insert(len(num),str(calcolo(s,par,aP)[0]))  
         
        P=False
        l=""
if P==False:
    if x==len(s)-1 and pr==1:
         num.insert(len(num),l)
    elif x==len(s)-1 and pr==3:
        num.insert(1,l)
    elif x==len(s)-1 and pr==2 and flag==True:
        num.insert(2,l)
    elif x==len(s)-1 and pr==2 and flag==False:
        num.insert(1,l)     
       
print(calcolo(s,num,a))
