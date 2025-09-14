# TypeError
# These errors occur when you are using the wrong data type. e.g. len(12345)
# Because you can only give the len() function Strings, it will refuse to work and
# give you a TypeError if you give it a number (Integer)

#Task 1: Fix the len() function so it has no more warnings or errors.
len("Country")

# Type Checking
# You can check the data type of any value or variable in python using the type() function.

print(type("abc"))     #It will give you <class 'str'>
print(type(True))       #It will give you <class 'bool'>

#Task 2:  Write out 4 type checks to print all 4 data types
print(type("hello"))
print(type(21))
print(type(15.6))
print(type(True))

# Type Conversion
# You can convert data into different data types using special functions. e.g.

# float() , int() , str() , bool()

print(int("123")+int("456"))    # Result will be sum of these numbers i.e., 579

#print(int("abc")+int("456"))      ValueError

#Task 3: Make this line of code run without errors The below line will give TypeError
# print("Number of letters in your name: " + len(input("Enter your name")))
#String concatenation (using the + operator) only works between strings.

print("Number of letters in your name:" +str(len(input("Enter your name "))))

