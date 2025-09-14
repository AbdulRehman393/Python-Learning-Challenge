import math
bmi = 84 / 1.65 ** 2
print(bmi)

#Number Manipulation

#Flooring  a number means rounding it down to the nearest integer , regarding whether the number
# is positive or negative
print(math.floor(bmi)) #We need to import math module to use floor function

#Rounding  a number means anything above 0.5 , it will round up  and anything below 0.5 it will
# round down.
print(round(bmi))

print(round(bmi,2))  #It will round upto two decimal places

#Assignment Operators

# Assignment operators such as the addition assignment operator += will add the number on the right
# to the original value of the variable on the left and assign the new value to the variable.
# +=  , -= ,*= , /=

score =0
#User scors a point
score += 1   #  it is short form of score = score +1
score -=1    # Same as score = score - 1

# f-Strings
# We can use f-strings to insert a variable or an expression into a string
# This makes it really easy to mix strings and different data types

points = 1
height = 5.10
is_winning = True

print(f"Your current score is {points}, Your height is {height}, You are winning is {is_winning}")




