# Project Treasure Island
print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
     
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at cross road. Where do you want to go?")
direction = input("\t Type 'left' or 'right': ")
direction = direction.lower()

if direction == "left":
    print("We have come to a Lake, There is an island in the middle of the lake")
    response = input("Type 'wait' to wait for a boat, type 'swim' to swim across: ")
    response = response.lower()
    if response == "wait":
       door = input(r'''You arrive at the island unharmed. There is a house with 3 doors. 
       One red, one yellow and one blue. Which colour do you choose? ''')
       door = door.lower()
       if door == "red":
           print("Burned by fire. Game Over!")
       elif door == "blue":
           print("Eaten by beasts. Game Over!")
       elif door == "yellow":
           print("You Win!")
       else:
           print("Game Over!")

    else:
        print("Attacked by trout. Game Over!")

else:
    print("Fall into a hole, Game Over")