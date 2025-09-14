#Logical Operators = You can combine different
#conditions using logical operators.
# A and B #Both conditions need to be true
# C or D #Only one condition needs to be true
# not E #The condition must be false

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    elif age > 18 and age < 45:
        bill = 12
        print("Adult tickets are $12.")

    elif age >= 45 and age <=55:  #You can also write it as 45 <= age <=55
        bill=0
        print("Your ticket price is free")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

