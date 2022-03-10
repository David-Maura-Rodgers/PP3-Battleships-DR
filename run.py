# TO RUN CODE: python3 run.py
# from random import randomint

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
print("Com Guess: [3, 1, 4, 5]")
print("Com Guess: [2, 4, 2, 5]\n")
print("The 1st number is the COLUMN, and the 2nd number is the ROW: \n")
print("NOTE: Please only select from numbers 1 to 5\n")

# While Loop to count number of ships placed by player
ship_placement = False
ship_number = 0

# https://stackoverflow.com/questions/4435169/how-do-i-append-one-string-to-another-in-python#comment88685663_4435169
# Lists to hold cordinates for player's x and y coordinates
player_position_x = []
player_position_y = []


def check_computer_guess():
    '''
    Function to check computer guess
    '''

    # STATIC TEST DATA TO CHECK THAT IF STATEMENT WORKS
    com_guess_x = [3, 1, 4, 5]
    com_guess_y = [2, 4, 2, 5]

    # Check computer guess against player first ship position
    if player_position_x[0] == com_guess_x[0]:
        if player_position_y[0] == com_guess_y[0]:
            print("Your First Ship has been hit!!!\n")
    else:
        print("Your missile missed its target . . .")

    # Check computer guess against player second ship position
    if player_position_x[1] == com_guess_x[1]:
        if player_position_y[1] == com_guess_y[1]:
            print("Your Second Ship has been hit!!!\n")
    else:
        print("Your missile missed its target . . .")

    # Check computer guess against player third ship position
    if player_position_x[2] == com_guess_x[2]:
        if player_position_y[2] == com_guess_y[2]:
            print("Your Third Ship has been hit!!!\n")
    else:
        print("Your missile missed its target . . .")

    # Check computer guess against player fourth ship position
    if player_position_x[3] == com_guess_x[3]:
        if player_position_y[3] == com_guess_y[3]:
            print("Your Fourth Ship has been hit!!!\n")
    else:
        print("Your missile missed its target . . .")


# Main Logic for game
while not ship_placement:
    input_x = int(input("Please select number for COLUMN: "))
    input_y = int(input("Please select number for ROW: "))
    print("\n")
    ship_number += 1
    player_position_x.append(input_x)
    player_position_y.append(input_y)

    # Convert both position inputs from string to integer
    # Updates board with the user input(position variables) and places @ there.
    horizontal = input_x
    vertical = input_y
    player_board[vertical - 1][horizontal - 1] = "@"

    if ship_number == 4:
        ship_placement = True
        print(' '.join(row1))
        print(' '.join(row2))
        print(' '.join(row3))
        print(' '.join(row4))
        print(' '.join(row5))
        print("\n")
        print(f"X Coordinates: {player_position_x}")
        print(f"Y Coordinates: {player_position_y}")
        print("All your ships have been placed!")
        print("\n")

check_computer_guess()
