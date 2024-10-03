import turtle

# Creare una finestra per disegnare
window = turtle.Screen()
window.bgcolor("white")

# Creare un oggetto turtle
cerchio = turtle.Turtle()
cerchio.shape("turtle")
cerchio.color("blue")
cerchio.speed(10)

# Definire il numero di parti del cerchio
num_parti = 12
angolo = 360 / num_parti

# Disegnare il cerchio diviso in parti
for _ in range(num_parti):
    cerchio.begin_fill()
    cerchio.circle(100, angolo)
    cerchio.setheading(cerchio.heading() + angolo)
    cerchio.end_fill()
