"""
Add more inputs (like player or team name).
Store each player's roll totals in separate arrays.
Choose a dice-based game that you can fully simulate using python.
"""
import random   
def main():
  # roll = random.randint(1,6)
  # print(f'You rolled a {roll}')
  dice_rolls = int(input("How many dice would you like to roll? "))
  dice_size = int(input("How many sides are the dice? "))
  dice_sum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1, 6)
    dice_sum += roll
    if roll == 1:
      print(f"You rolled a {roll}! Critical Fail!")
    elif roll == dice_size:
      print(f"You rolled a {roll}! Critical success!")
    else:
      print(f'You rolled a {roll}')
  print(f"You have rolled a total of {dice_sum}")
  return dice_sum

def player():
  player_one = True
  player_two = False
  player_one_dice_sum = 0
  player_two_dice_sum = 0
  
  print("Player one: ")
  player_one_dice_sum = main()
  print("Player Two: ")
  player_two_dice_sum =  main()
  print(f"Player one: {player_one_dice_sum}")
  print(f"Player two: {player_two_dice_sum}")
if __name__== "__main__":
  player()