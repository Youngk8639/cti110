import turtle
t = turtle.Turtle()

# Draw a square

for i in range(4):
t.forward(side)
t.left(90)
t.penup()
t.left(180)
t.forward(side*2)
t.pendown()

# Draw a triangle 
for i in range(3):
t.forward(side)
t.left(120)

t.exitonclick()