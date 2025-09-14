#Mathematical Operators
# +, -, *, /, // and **

print("My age: " + str(12)) #It will concatenate two strings
print(123+456)
print(7-3)
print(3*2)
print(6/3)    # Output: 2.0
print(6//3)   #Output: 2 , It first performs 6/3 and then remove decimal places
print(2**3)   #Output: 8, its access to exponent its like 2^3 or 2*2*2

#Order Precedence
# Follow PEDMAS Rule
#Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

# When deciding between same order operator like addition or subtraction, go from
# left to right (known as left-to-right associativity)

# TASK 1. What is the output of this code?
print(3 * 3 + 3 / 3 - 3)    #7.0

# TASK 2. Change the code so it outputs 3?
# print(3 * 3 + 3 / 3 - 3)

print(3*(3+3)/3-3)      #Output 3.0
print(3*(3+3)//3-3)
