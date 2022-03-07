# Player can place 4 ships at coordinates of their choosing
row1 = [".", ".", ".", ".", "."]
row2 = [".", ".", ".", ".", "."]
row3 = [".", ".", ".", ".", "."]
row4 = [".", ".", ".", ".", "."]
row5 = [".", ".", ".", ".", "."]

player_ships = []

player_board = [row1, row2, row3, row4, row5]

# Print board to player
print(' '.join(row1))
print(' '.join(row2))
print(' '.join(row3))
print(' '.join(row4))
print(' '.join(row5))
print("\n")

print("Please select where you want to place your ships\n")
print("The 1st number is the COLUMN, and the 2nd number is the ROW: \n")
print("Please only select from numbers 1 to 5\n")

# Variable to check number of ships placed by user
ship_placement = False
ship_number = 0

# Attempt at While Loop
while not ship_placement:
  position_one = input("Please select number for COLUMN: \n")
  position_two = input("Please select number for ROW: \n")
  ship_number += 1

  # Convert both position inputs from string to integer
  horizontal = int(position_one)
  vertical = int(position_two)

  # Updates board with the user input(position variables) and places @     there.
  player_board[vertical - 1][horizontal - 1] = "@"
  
  if ship_number == 4:
    ship_placement = True
    print(' '.join(row1))
    print(' '.join(row2))
    print(' '.join(row3))
    print(' '.join(row4))
    print(' '.join(row5))
    print("All ships have been placed!")

'''
# Convert both position inputs from string to integer
horizontal = int(position_one)
vertical = int(position_two)

# Updates board with the user input(position variables) and places @ there.
player_board[vertical - 1][horizontal - 1] = "@"

# https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
print(' '.join(row1))
print(' '.join(row2))
print(' '.join(row3))
print(' '.join(row4))
print(' '.join(row5))
'''

