# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# TO RUN CODE: python3 run.py

# from random import randomint

# Player can place 4 ships at coordinates of their choosing
row1 = [".", ".", ".", ".", "."]
row2 = [".", ".", ".", ".", "."]
row3 = [".", ".", ".", ".", "."]
row4 = [".", ".", ".", ".", "."]
row5 = [".", ".", ".", ".", "."]

player_board = [row1, row2, row3, row4, row5]

# Variables needed for main game logic
ship_placement = False
player_ship_number = 0

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

# Lists to hold cordinates for player's x and y coordinates
player_position_x = []
player_position_y = []


def check_computer_guess():
    '''
    Function to check computer guess against player's ships on board
    '''
    # Check computer guess against player first ship position
    # Check computer guess against player second ship position
    # # STATIC TEST DATA TO CHECK THAT IF STATEMENT WORKS
    com_guess_x = [3, 1, 4, 5]
    com_guess_y = [2, 4, 2, 5]

    # Variables
    player_lives = 4
    should_continue = True

    while should_continue:
        if player_position_x[0] == com_guess_x[0]:
            if player_position_y[0] == com_guess_y[0]:
                player_lives -= 1
                print(player_lives)
                print("Your First Ship has been hit!!!\n")
        else:
            print(player_lives)
            print("Your missile missed its target . . .")
      
        if player_position_x[1] == com_guess_x[1]:
            if player_position_y[1] == com_guess_y[1]:
                player_lives -= 1
                print(player_lives)
                print("Your Second Ship has been hit!!!\n")
        else:
            print(player_lives)
            print("Your missile missed its target . . .")

    # Check computer guess against player third ship position
        if player_position_x[2] == com_guess_x[2]:
            if player_position_y[2] == com_guess_y[2]:
                player_lives -= 1
                print(player_lives)
                print("Your Third Ship has been hit!!!\n")
        else:
            print(player_lives)
            print("Your missile missed its target . . .")

    # Check computer guess against player fourth ship position
        if player_position_x[3] == com_guess_x[3]:
            if player_position_y[3] == com_guess_y[3]:
                player_lives -= 1
                print(player_lives)
                print("Your Fourth Ship has been hit!!!\n")
        else:
            print(player_lives)
            print("Your missile missed its target . . .")

        if player_lives == 0:
            print("All your ships have been destroyed")
            should_continue = False


# Main Logic for game
while not ship_placement:
    input_x = int(input("Please select number for COLUMN: "))
    input_y = int(input("Please select number for ROW: "))
    print("\n")
    player_ship_number += 1
    player_position_x.append(input_x)
    # print(player_position_x)
    player_position_y.append(input_y)
    # print(player_position_y)

    # Convert both position inputs from string to integer
    # Updates board with the user input(position variables) and places @ there.
    horizontal = input_x
    vertical = input_y
    player_board[vertical - 1][horizontal - 1] = "@"

    if player_ship_number == 4:
        ship_placement = True
        print("   COLUMN")
        print("  " + ' '.join(row1))
        print("R " + ' '.join(row2))
        print("O " + ' '.join(row3))
        print("W " + ' '.join(row4))
        print("  " + ' '.join(row5))
        print("\n")
        print(f"X Coordinates: {player_position_x}")
        print(f"Y Coordinates: {player_position_y}")
        print("All your ships have been placed!")
        print("\n")

check_computer_guess()
