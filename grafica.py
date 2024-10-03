import turtle
num= int(input( "Inserisci il numero dei lati "))
angle=360/num

for x in range(num):
    turtle.right(angle)
    turtle.fd(300)
turtle.done()
    


