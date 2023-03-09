#===========
# VARIABLES
#===========
# Variables are like addresses that point to a place in the systems memory where data is stored
# In python there isn't any command that is needed to declare a a new variable
# The name of the variable doesn't have to be specific, but the name should be relevant to the program and whats store in it
# In Python they can be reasigned as many times needed
# This is just a few examples of working with variables

num = 2

num = "string"

# print(num)

#============
# Data Types
#============
# There are multiple different data type, and data structures.
# They are used throught most other commonly used programing languages
# They all have their purposes, and in many languages the prebuilt methods, much like turtle
# The names and methods of these types can be different in varying languanges
# These a few of the more commonly used data types/structures 

# STRINGS => string of characters inside quotaions
str = "Hello World  12 !"

# INTEGERS => whole numbers
num = 12

# FLOATS => numbers with decimals
num2 = 1.2121

# BOOLEANS => True or False
is_valid = True
is_not_valid = False

# DICTIONARIES => Key Value Pairs stored in {}
myDict = {
    "first_name": "Mr",
    "last_name": 636,
    "is_above_18": True,
    "garage": ["zo6", "ZX6R", "Jeep"],
    "date_of_birth": {
        "year": 1999,
        "month": "March",
        "day": 11
    }
}


# print(myDict)
# print(myDict["garage"])
# print(myDict["date_of_birth"]["year"])


# LISTS = multiple data types or structures stored in []
myList = [
    "Hi", # 0
    33, # 1
    False,
    11.222,
    ["a","b",1],
    {"a":1,"b":4,"c":"d"}
]

# print(myList)
# print(myList[0])
# print(myList[4][1])
# print(myList[5]["b"])



# ==========
# OPERATORS
# ==========
# + Addition
# sum = x + y => 6 = 3 + 3

# - Subtraction
# sum = x - y => 0 = 3 - 3

# * Multiplication
# sum = x * y => 9 = 3 * 3

# / Division
# sum = x / y  => 1 = 3 / 3

# ** Exponentiation
# sum = x ** y  => 27 = 3 ** 3 or 3*3*3

# // floor division (rounds down to nearest whole #)
# sum = x // y  => 1 = 4 // 3


# % modulus, will divide two integers and returns the remainder
# sum = x % y  => 1 = 5 % 2

# += adds a value to an existing Variable or concatenate
# sum = 3
# sum += 3 => 6 = 3 + 3

# -= subtracts a value to an existing Variable
# sum = 3
# sum -= 3 => 0 = 3 - 3

# ==, is, checks if two values are equale
# 3 == 3  => True
# 2 == 3  => Flase

# !=, is not, checks if two values are not equale
# 2 != 3  => True
# 3 != 3  => Flase

# > , checks if first value is greater than second value
# 4 > 3  => True
# 2 > 3  => Flase

# >=, checks if first value is greater than or equals second value
# 4 >= 3  => True
# 3 >= 3  => True
# 2 >= 3  => Flase

# <, checks if first value is less than second value 
# 2 < 3  => True
# 4 < 3  => Flase

# <=, checks if first value is less than or equals second value
# 2 <= 3  => True
# 3 <= 3  => True
# 4 <= 3  => Flase

# in, checks if one value is in another value
# "hello" in "hello world" => True
# "hello" in "world" => False

# not in, checks if one value is not in another value
# "hello" not in "hello world" => False
# "hello" not in "world" => True

# AND, &, checks two operators, returns true if both are true
# 1 == 1 AND 2 == 2 => True
# 1 == 1 & 2 == 2 => True
# 1 == 2 AND 2 == 2 => False

# OR, |, checks two operators, returns true if either or both are true
# 1 == 1 OR 2 == 2 => True
# 1 == 1 | 2 == 2 => True
# 1 == 1 OR 3 == 2 => True
# 1 == 2 OR 3 == 2 => False