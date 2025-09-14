print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill=0
size = size.upper()
pepperoni = pepperoni.upper()
extra_cheese = extra_cheese.upper()

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill +=2

elif size == "M":
    bill = 20
    if pepperoni =="Y":
        bill +=3

elif size == "L":
    bill = 25
    if pepperoni =="Y":
        bill +=3

else:
    print("You have entered invalid pizza size")

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")



