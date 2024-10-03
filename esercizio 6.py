num = [1,2,0,0,3,4,5,-1,0,2,-1,-3,0,0,0,0,0,0,0,0,2,-3,-4,-5,0,0,0]
sequenza = 0
prev = 0
conto = []
for i in range(len(num)):
    if num[i] == 0:
        sequenza += 1
        conto += sequenza
    else:            
      if sequenza > prev:
        prev = zero
      zero = 0

print(str(prev))

#index = 2
#new_char = "$"


