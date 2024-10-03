import random
cont=[0,0,0,0,0,0,0,0,0,0,0]
prob=[0,0,0,0,0,0,0,0,0,0,0]
for x in range(10000):
    dado=random.randint(1,6)
    dado1=random.randint(1,6)
    cont[dado+dado1-2] += 1
print(cont)
for x in range(11):
    prob[x]=cont[x]/10000*100
    
y=2
for x in prob:
    
    
    print("numero: ",y,"percentuale: ",x,"%")
    y+=1