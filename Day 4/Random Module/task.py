import random

random_integer = random.randint(1,10)  # it will generate numbers between 1 and 10
print(random_integer)                        # both 1 and 10 are included.

random_0_to_1 = random.random()              # it will generate between 0 and 1
print(random_0_to_1)                                             # 0 is inclusive and 1 is not inclusive

random_0_to_10 = random.random() * 10        # it will generate random number between 0 and
print(random_0_to_10)                        # 10 , 0 is inclusive and 10 not inclusive

random_float = random.uniform(1,10)    # it will generate random number between 1 and 1o
print(random_float)                          # the lower bound in inclusive but because of floating
                                             # point precision, it's very rare to get exactly 10.0.

#Task 1: PAUSE 1 - Heads or Tails
#Create a coin flip program using what you have learnt about randomisation
# in Python. It should randomly print "Heads" or "Tails" everytime it is run.

if random.randint(0,1)==1:
    print("Heads")
else:
    print("Tails")



