
def piramide(n,k):
    
    
    if k==0 or k==n:
        return 1
    
 
    
    
    
    else:
        
        return piramide(n-1,k-1)+piramide(n-1,k)
     

    
    
    
    



n=int(input ("Inserisci n "))
k=int(input("Inserisci k "))

print(piramide(n,k))