import random
num=int(input("Inserisci il numero di alunni "))

nomi=["Carlo","Franco","Francesco","Giovanni","Francesca","Paola"]
for x in range(num):
    print("alunno: ",nomi[random.randint(1,6)])
    print("Voti: ")
    for x in range(5):
        voto=random.randint(1,10)
        print(voto)