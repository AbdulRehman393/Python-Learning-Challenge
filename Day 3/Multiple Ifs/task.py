print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill =0
if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Your ticket price is $5.")
    elif age <= 18:
        bill = 7
        print("Your ticket price is  $7.")
    else:
        bill = 12
        print("Your ticket price is $12.")

    want_photo = input("Do you want photo? Type Y for yes and N for No")

    if want_photo.upper()=="Y":
        bill += 3
        print(f"Your total  bill is {bill}")
    else:
        print(f"Your total bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
