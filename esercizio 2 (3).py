
num=int(input("Inserisci il numero di numeri da inserire "))
num2=[]

ver=0

indice=[]

for x in range(num):
    num2.insert(x,int(input("Inserisci il numero ")))
    if num2[x]==0:
        indice.insert(len(indice),x)
       
        ver=1

    
    

if ver==1:  
    cont=1
    app=0
    for x in range(len(indice)-1):
    
    
        if indice[x+1]-indice[x]==1:
            cont+=1
        else:
            cont=1
        if cont>app:
                app=cont
                
    
    print(app)    
        

    
    
        


    