import random
import time

v = input("Enter your name: ")
print("You are Player 1")
h = input("Enter your name: ")
print("You are Player 2")


def roll_dice():
  return random.randint(1, 6)


def snake_ladder(position):
  snakes_and_ladders = {
      5: 48,
      9: 30,
      20: 42,
      42: 16,
      27: 58,
      36: 95,
      41: 79,
      42: 16,
      49: 71,
      69: 94,
      16: 6,
      47: 26,
      49: 11,
      56: 53,
      62: 19,
      64: 60,
      87: 24,
      93: 73,
      95: 75,
      98: 78
  }
  return snakes_and_ladders.get(position, position)


def display_board(player1, player2):
  print("Player 1 is at position : ", player1)
  print("Player 2 is at position : ", player2)
  print("-------------------------------")


def snake_ladder_game():
  player1, player2 = 1, 1

  while True:
    print("Player 1")
    input("Press Enter to roll the dice...")
    print("Loding.....")
    time.sleep(1)
    dice_roll = roll_dice()
    print("Dice Roll:", dice_roll)

    player1 += dice_roll
    player1 = snake_ladder(player1)

    display_board(player1, player2)

    if player1 >= 100:
      print(f"   \333 {v} wins! \333")
      break
    print("Turn to Player 2")
    input("Press Enter to roll the dice...")
    print("Loding.....")
    time.sleep(1)
    dice_roll = roll_dice()
    print("Dice Roll:", dice_roll)

    player2 += dice_roll
    player2 = snake_ladder(player2)

    display_board(player1, player2)

    if player2 >= 100:
      print(f"   \333 {h} wins! \333")
      break


if __name__ == "__main__":
  print("\nWelcome to Snake and Ladder Game!")
  time.sleep(1)
  print("Snake position on : 16, 42, 47, 49, 56, 62, 64, 87, 93, 95, 98")
  time.sleep(1)
  print("Ladder position on : 5, 9, 20, 27, 36, 41, 49, 69")
  time.sleep(1)
  snake_ladder_game()
