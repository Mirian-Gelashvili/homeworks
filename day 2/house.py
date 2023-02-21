from turtle import *


# we want to paint a house


color("red")
width(10)

# Step 1 drawing Square
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

# Step 2 Drawing a door


forward(70)
width(5)
color("green")
left(90)
forward(80)

right(90)
forward(40)

right(90)
forward(80)

right(90)
forward(40)

# Step 3 drawing roof
color("brown")
width(10)
penup()
goto(200,200)
pendown()


right(60)
forward(200)
left(120)
forward(200)

# Step 4 Drawing Windows

penup()
goto(20,110)
pendown()

right(150)
forward(60)

right(90)
forward(60)

right(90)
forward(60)

right(90)
forward(60)

exitonclick()

