from turtle import *

# Basic Movement
fd(100)
rt(45)
bk(20)
lt(35)
fd(30)
home()
clearscreen()

# Setting Position
goto(80,80)
setpos(-80, 80)
setx(0)
sety(0)
clearscreen()

# Setting Heading
    # 0 - east
    # 90 - north
    # 180 - west
    # 270 - south
setheading(90)
seth(270)
seth(299) # south east south


# The Circle Method
circle(200)
circle(112,180)
home()
circle(100, 360, 5)
clearscreen()

# The Dot Method
fd(100)
dot(15, "green")
rt(100)
fd(100)
dot(30, "blue")
rt(98)
fd(60)
dot(25, "red")
clearscreen()

# Using Stamps
fd(100)
rt(90)
first_stamp = stamp()
print(first_stamp)
fd(100)
rt(90)
stamp()
fd(100)
rt(90)
stamp()
fd(100)
rt(90)
stamp()
fd(50)
# clearstamp(28)
# clearstamps()
# clearstamps(2)
# clearstamps(-2)

# Undo Moves
undo()
undo()
undo()
undo()
undo()
clearscreen()

# Speed
    # speen takes an number 0-10, 1 being the slowest and increasing in speed to 10
    # 0 is the fastest speed, if the value entered in greater than 10 or less than 1 it will default to 0
    # we can also use actual word in "", "slowest", "slow", "normal", "fast", "fastest" 
speed(1)
fd(100)
bk(100)

speed("normal")
rt(30)
fd(100)
bk(100)

speed(0)
circle(100)
rt(2)
circle(100)
rt(2)
circle(100)



done()