import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

allowed_directions = [NORTH, EAST, SOUTH, WEST]
allowed_choices = ["y", "n"]

def move(direction, col, row):
     ''' Returns updated col, row given the direction '''
     if direction == NORTH:
          row += 1
     elif direction == SOUTH:
          row -= 1
     elif direction == EAST:
          col += 1
     elif direction == WEST:
          col -= 1
     return(col, row)

def is_victory(col, row):
     ''' Return true if player is in the victory cell '''
     return col == 3 and row == 1  # (3,1)

def print_directions(directions_str):
     print("You can travel: ", end='')
     first = True
     for ch in directions_str:
          if not first:
               print(" or ", end='')
          if ch == NORTH:
               print("(N)orth", end='')
          elif ch == EAST:
               print("(E)ast", end='')
          elif ch == SOUTH:
               print("(S)outh", end='')
          elif ch == WEST:
               print("(W)est", end='')
          first = False
     print(".")


def pull_a_lever(col, row, coin):
     if (col == 1 and row == 2) or (col == 2 and row == 2) or (col == 2 and row == 3) or (col == 3 and row == 2):
          user_input = random.choice(allowed_choices)

          print("Pull a lever (y/n):", user_input)

          if user_input == 'y':
               coin += 1
               print("You received 1 coin, your total is now {}.".format(coin))
     
     return coin

def find_directions(col, row):
     ''' Returns valid directions as a string given the supplied location '''
     if col == 1 and row == 1:   # (1,1)
          valid_directions = NORTH
     elif col == 1 and row == 2:  # (1,2)
          valid_directions = NORTH+EAST+SOUTH
     elif col == 1 and row == 3:  # (1,3)
          valid_directions = EAST+SOUTH
     elif col == 2 and row == 1:  # (2,1)
          valid_directions = NORTH
     elif col == 2 and row == 2:  # (2,2)
          valid_directions = SOUTH+WEST
     elif col == 2 and row == 3:  # (2,3)
          valid_directions = EAST+WEST
     elif col == 3 and row == 2:  # (3,2)
          valid_directions = NORTH+SOUTH
     elif col == 3 and row == 3:  # (3,3)
          valid_directions = SOUTH+WEST
     return valid_directions

def play_one_move(col, row, valid_directions, coin, moves):
     ''' Plays one move of the game. Return if victory has been obtained and updated col,row '''
     victory = False
     direction = random.choice(allowed_directions)
     
     print("Direction:", direction)
     
     direction = direction.lower()

     moves += 1

     if not direction in valid_directions:
          print("Not a valid direction!")
     else:
          col, row = move(direction, col, row)
          coin = pull_a_lever(col, row, coin)
          victory = is_victory(col, row)

     return victory, col, row, coin, moves

def play():
     # The main program starts here
     while True:
          victory = False
          row = 1
          col = 1
          coin = 0
          moves = 0
          seed_input = int(input("Input seed: "))
          seeder = random.seed(seed_input)

          while not victory:
               valid_directions = find_directions(col, row)
               print_directions(valid_directions)
               victory, col, row, coin, moves = play_one_move(col, row, valid_directions, coin, moves)
          print("Victory! Total coins {}. Moves {}.".format(coin, moves))

          again = (input("Play again (y/n): ")).lower()
          if again != "y":
               break

play()
