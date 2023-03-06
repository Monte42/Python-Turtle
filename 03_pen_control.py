from turtle import *

speed(1) # set turtle speed to slow

fd(50) 
penup() # lifts pen so turtle can move with drawing
fd(50)
rt(45)
pendown() # sets pen down so turtle will draw again
fd(50)
pu() # lifts pen so turtle can move with drawing
fd(50)
pd() # sets pen down so turtle will draw again
fd(50)
rt(90)
up() # lifts pen so turtle can move with drawing
fd(50)
down() # sets pen down so turtle will draw again
fd(50)

rt(45)
pensize(5) # sets the width of the pen or line
fd(25)
width(7) # sets the width of the pen or line
fd(25)

# isdown() is a method that will return a value of true/down or false/up
print(isdown()) # will print true
penup()
print(isdown()) # will print false



done()