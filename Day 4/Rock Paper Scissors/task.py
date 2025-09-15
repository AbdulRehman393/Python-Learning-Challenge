import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper, scissors]
user_option = int(input("What do you choose , type 0 for Rock, 1 for Paper or 2 for Scissors: "))


if user_option < 0 or user_option > 2:
    print("You typed an invalid number. You lose!")
else:
    print("You chose:")
    print(game_images[user_option])

computer_choice = random.randint(0,2)
print(f"Computer Choice: {game_images[computer_choice]}")

if user_option == computer_choice:
     print("It's a draw!")

elif user_option == 0 and computer_choice == 2:
    print("You win!")

elif user_option == 1 and computer_choice == 0:
     print("You win!")

elif user_option == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")

