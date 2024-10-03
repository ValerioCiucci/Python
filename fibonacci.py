
def fibonacci(num,app):
    
    
    
    if num>1:
        return (fibonacci(num-1,app)+fibonacci(num-2,app))
    
    
    
    
    elif num==0:
        return 0
    else:
        
        return 1/fibonacci1(app)

def fibonacci1(num):
    if num>1:
        return fibonacci1(num-1)+fibonacci1(num-2)
    elif num==0:
        return 0
    else:
        return 1


    


num=int(input("Inserisci un numero "))
print(fibonacci(num,num-1))
