#Banker Roulette
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#choice_1
random_number = random.randint(0,4)
print(f"{friends[random_number]} will pay the bill." )

#choice_2
print(f"{random.choice(friends)} will pay the bill.")
