import random
tot=0

for x in range(10):
    tot=random.randint(1,6)+ tot

if tot>35:
    print("Il risultato e' sopra la media ")
else:
    print("Il risultato non e' sopra la media ")