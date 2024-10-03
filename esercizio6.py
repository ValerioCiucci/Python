anno= input("Inserisci un anno ")
if anno%4==0 and anno%100==1:
    print("Quest anno è bisestile")
elif anno%400==0:
      print("Quest anno è bisestile")
else:
     print("Quest anno non è bisestile")

