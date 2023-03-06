from turtle import * # <-- the * means all

speed(1)

pensize(3)

# passing in the word value inside of ""
pencolor("red") # sets the outline of turtle and the color of the line turtle will draw
fd(100)
rt(90)

# passing decimal 3 values between .0 -.9 inside ()
pencolor((.0, .8, .0)) # RGB or red green blue / 0.0 - 0.9 / 0.0 = no color or darker, 0.9 = full color or lighter
fd(100)
rt(90)
pencolor((.0, .0, .8)) # RGB or red green blue / 0.0 - 0.9 / 0.0 = no color or darker, 0.9 = full color or lighter
fd(110)
rt(90)
pencolor((.0, .0, .0)) # RGB or red green blue / 0.0 - 0.9 / 0.0 = no color or darker, 0.9 = full color or lighter
fd(110)
rt(90)
pencolor((.7, .7, .7)) # RGB or red green blue / 0.0 - 0.9 / 0.0 = no color or darker, 0.9 = full color or lighter
fd(120)
rt(90)

# passing in a hexadecimal - EXAMPLE #112233 - need to be ""
pencolor("#12a7aa") # this is a 6 digit value that is prefixed with a #. Each digit is 0-9 or a-f
fd(120)
rt(90)
pencolor("#00ff00") # the first to digits represent red, digits 3&4 represent green, 5&6 represent blue
fd(130)
rt(90)
pencolor("#ddd") # 0 = lighter and f = darker 
fd(130)
rt(90)
pencolor("#333") # if only 3 digits are give they act as two, so this is the same as "#333333" 
fd(130)


# FILLING 
fillcolor("purple") # set the inside color of our turtle and can be used to fill a closed shape we draw
begin_fill()
circle(25) 
end_fill()

# setting both colors at once
home()
color("yellow", "#aa1122") # first value sets the pen color and the second value sets the fill color
begin_fill()
circle(25)
end_fill()

setpos(100,100)

reset() # reset the turtle position to home and also going to clear the screen


done()