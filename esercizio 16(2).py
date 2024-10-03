import random

num=int(input("Inserisci un numero "))

for x in range(5):
    tom=random.randint(1,90)
    print(tom)
    
    if num==tom:
        print("Complimenti hai vinto ")
        