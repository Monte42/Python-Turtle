# When we are writing code it is very common that we will use the code more than once.
# This can lead to very long or large files that quickly becomes hard to debug.
# As a programmer we dont want to repeat ourselves or write DRY code (dont repeat yourself)
# The way we achieve this is by using functions.
# functions are segments of code that we know we will use again and again.
# Like variables we must name our functions, the name can be anything, but should be specific to what it does.
# In Python  we declare function by prefixing the name with the command def
# NOTE: Indentation is important!

ext_cont = "From Turtle" # This is outside any function so it is a Global Var, so it can be called anywhere after it has been defined

def print_hello(message): # Also note that we use an underscore to seperate words in our function name
    # Also note the (), inside the ( ), we can pass in "arguments" that can be used in our code.
    # we finish the declaration with :
    # we can create variables inside the function. These are considered Local vars, meaning they only exist in the function
    hello_phrase = "hello world"
    print(hello_phrase + " " + ext_cont + " " + message)


# Once the function is complete we un indent our code to continue to write our app
# we can then call the function kind of like how we call functions

# print_hello("and from Mr 636") # we just need to add the () at the end


# LOOPS, this is how we run chucks of code repetitively
# there are two basic loops, For Loop and While Loops

# for i in range(2,10):
#     print(i)
#     print_hello("in a loop")

# num = 0
# while(num <= 10): # this will be true forever, the code will run until the condition is prove false
#     print(num)
#     num += 1

age = 14


if (age>18):
    print("Old enough")
elif (age == 18):
    print("just old enough")
else:
    print("Too Young")