# TO RUN CODE: python3 run.py
# from random import randomint

# Player can place 4 ships at coordinates of their choosing
# Player can place 4 ships at coordinates of their choosing
row1 = [".", ".", ".", ".", "."]
row2 = [".", ".", ".", ".", "."]
row3 = [".", ".", ".", ".", "."]
row4 = [".", ".", ".", ".", "."]
row5 = [".", ".", ".", ".", "."]

player_board = [row1, row2, row3, row4, row5]

# Print board to player
print("   COLUMN")
print("  " + ' '.join(row1))
print("R " + ' '.join(row2))
print("O " + ' '.join(row3))
print("W " + ' '.join(row4))
print("  " + ' '.join(row5))
print("\n")

print("Place your ships at four different coordinates on the board.")
print("The 1st number is the COLUMN, and the 2nd number is the ROW: \n")
print("NOTE: Please only select from numbers 1 to 5\n")

# While Loop to count number of ships placed by player
ship_placement = False
ship_number = 0

# https://stackoverflow.com/questions/4435169/how-do-i-append-one-string-to-another-in-python#comment88685663_4435169
# Lists to hold cordinates for player's x and y coordinates
position_x = []
position_y = []

while not ship_placement:
    input_x = int(input("Please select number for COLUMN: "))
    input_y = int(input("Please select number for ROW: "))
    ship_number += 1
    x = position_x.append(input_x)
    y = position_y.append(input_y)
    print(position_x)
    print(position_y)

    # Convert both position inputs from string to integer
    # Updates board with the user input(position variables) and places @ there.
    horizontal = int(input_x)
    vertical = int(input_y)
    player_board[vertical - 1][horizontal - 1] = "@"

    if ship_number == 4:
        ship_placement = True
        print(' '.join(row1))
        print(' '.join(row2))
        print(' '.join(row3))
        print(' '.join(row4))
        print(' '.join(row5))
        print("\n")
        print("All your ships have been placed!")
        print("\n")

