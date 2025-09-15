#For Loops with Range
# The combination of the range() function with the Python For Loop allows us to
# run a loop for as many times as we wish. Instead of looping through each item in a List,
# we can loop through a range of numbers.

#By Default, the range() function will step through all the numbers from start to the end , and
# it will increase by 1.
for number in range(1,10):   # This is going to be number between 1 and 10, 10 is not included.
    print(number)

# if you wanted to increase by any other number , then you have to do like it.
for numbers in range(1,11,3):
    print(numbers)

# write a number to add numbers from 1 to 100 by using for loo[ss
Sum = 0
for number in range (1,101):
    Sum += number
print(Sum)
