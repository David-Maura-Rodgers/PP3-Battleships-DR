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
print(' '.join(row1))
print(' '.join(row2))
print(' '.join(row3))
print(' '.join(row4))
print(' '.join(row5))
print("\n")

print("Place your ships at four different coordinates on the board")
print("The 1st number is the COLUMN, and the 2nd number is the ROW: \n")
print("NOTE: Please only select from numbers 1 to 5\n")


# While Loop to count number of ships placed by player
ship_placement = False
ship_number = 0
position_one = []
position_two = []
position_three = []
position_four = []

while not ship_placement:
    coord_one = input("Please select number for COLUMN: ")
    coord_two = input("Please select number for ROW: ")
    print("\n")
    ship_number += 1

    # Convert both position inputs from string to integer
    # Updates board with the user input(position variables) and places @ there.
    horizontal = int(coord_one)
    vertical = int(coord_two)
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

# For Loop for player coordinates
# Store player coordinates in two Lists
player_coord_x = []
player_coord_y = []

for coord in coord_one:
    player_coord_x += coord
print(player_coord_x)

for coord in coord_two:
    player_coord_y += coord
print(player_coord_y)
