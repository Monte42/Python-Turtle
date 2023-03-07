from turtle import *

speed(1)
fd(100)
rt(90)
hideturtle() # this will hide the turtle but it will still draw
print(isvisible()) # this will return true if the turtle is visable, otherwise it will return false // false
fd(100)
rt(90)
showturtle() # this will show the turtle again
print(isvisible()) # this will return true if the turtle is visable, otherwise it will return false // true
fd(100)
rt(90)
ht() # this will hide the turtle but it will still draw
fd(100)
rt(90)
st() # this will show the turtle again
fd(110)
rt(90)

color('blue', 'green')
shape("turtle") # this will change the shape of the turtle
fd(110)
rt(90)

shapesize(2,2,2) # this will change the scale of the turtle, this first value will multipy its width, second its length, third its outline
# turtlesize() this is the same as shapesize

shearfactor(0.8) # this is going to skew the turtle
fd(110)
rt(90)

shearfactor(0.1)
tilt(180) # this will take an angle, this will rotate the turtle by that amount of degrees
fd(120)


done()
