# Write your code to expect a terminal of 80 characters wide and 24 rows high
# TO RUN CODE: python3 run.py

import random

# GLOBAL SCOPE NEEDED FOR ALL FUNCTIONS TO ACCESS THESE VARIABLES
player_position_x = []
player_position_y = []
com_lives = 4
player_lives = 4
player_missile_x = None
player_missile_y = None
game_over = False

# RANDOM ENEMY SHIP POSITION IN rand_enemy_ships Function
com_position_x = random.sample(range(1, 6), 4)
com_position_y = random.sample(range(1, 6), 4)

# RANDOM ENEMY SHIP MISSILE GUESS
enemy_missile_x = random.sample(range(1, 6), 1)
enemy_missile_y = random.sample(range(1, 6), 1)


# ------ STARTS THE GAME ------------- \\
def play_game():
    '''
    Function: Starts the game: prints board to player etc
    '''
    ship_placement = False
    player_ship_number = 0
    print("\n")
    print("Place your ships at four different coordinates on the board.")
    print("The 1st number is the COLUMN, and the 2nd number is the ROW: \n")
    print("NOTE: Please only select from numbers 1 to 5\n")

    row1 = [".", ".", ".", ".", "."]
    row2 = [".", ".", ".", ".", "."]
    row3 = [".", ".", ".", ".", "."]
    row4 = [".", ".", ".", ".", "."]
    row5 = [".", ".", ".", ".", "."]

    player_board = [row1, row2, row3, row4, row5]

    print("   COLUMN")
    print("  " + ' '.join(row1))
    print("R " + ' '.join(row2))
    print("O " + ' '.join(row3))
    print("W " + ' '.join(row4))
    print("  " + ' '.join(row5))
    print("\n")

    while not ship_placement:
        input_x = int(input("Please select number for COLUMN: "))
        input_y = int(input("Please select number for ROW: "))
        print("         - - - - - - -        ")
        player_ship_number += 1
        player_position_x.append(input_x)
        player_position_y.append(input_y)
        horizontal = input_x
        vertical = input_y
        player_board[vertical - 1][horizontal - 1] = "@"

        if player_ship_number == 4:
            ship_placement = True
            print("\n")
            print("   COLUMN")
            print("  " + ' '.join(row1))
            print("R " + ' '.join(row2))
            print("O " + ' '.join(row3))
            print("W " + ' '.join(row4))
            print("  " + ' '.join(row5))
            print("\n")
            print("ALL YOU SHIPS HAVE BEEN PLACED:")
            print(f"Player Ship X Coordinates: {player_position_x}")
            print(f"Player Ship Y Coordinates: {player_position_y}")  
            print("\n")

            return player_position_x
            return player_position_y


# --- CREATE RANDOM COM SHIP COORDINATES ------ //
def rand_enemy_ships():
    '''
    Function to place enemy ship coordinates at random
    '''
    # Create random sample of computer ship positions
    global com_position_x
    global com_position_y 
    print("All ENEMY SHIPS HAVE BEEN PLACED:")
    print(f"Com ship X Coordinates: {com_position_x}")
    print(f"Com ship Y Coordinates: {com_position_y}\n")


# --- ASK PLAYER TO SHOOT MISSILE AT ENEMY POSITIONS --- //
# --- CHECK PLAYER MISSILE AGAINST COM SHIP POSITIONS --- \\
def check_player_missile(player_missile_x, player_missile_y):
    '''
    Function to check computer guess against player's ships on board
    '''
    print("TIME TO FIRE YOUR MISSILE AT THE ENEMY!\n")
    global com_lives
    should_continue = True
    while should_continue:
        player_missile_x = int(input("Select X coordinates to fire: "))
        player_missile_y = int(input("Select Y coordinates to fire: "))
        print("\n")
        if player_missile_x == com_position_x[0]:
            if player_missile_y == com_position_y[0]:
                com_lives -= 1
                print("You have hit the ENEMY'S first ship!!!\n")
                print(f"Enemy Ships Left: {com_lives}\n") 
        if player_missile_x == com_position_x[1]:
            if player_missile_y == com_position_y[1]:
                com_lives -= 1
                print("You have hit the ENEMY'S second ship!!!\n")
                print(f"Enemy Ships Left: {com_lives}\n")
        if player_missile_x == com_position_x[2]:
            if player_missile_y == com_position_y[2]:
                com_lives -= 1
                print("You have hit the ENEMY'S third ship!!!\n")
                print(f"Enemy Ships Left: {com_lives}\n")
        if player_missile_x == com_position_x[3]:
            if player_missile_y == com_position_y[3]:
                com_lives -= 1
                print("You have hit the ENEMY'S fourth ship!!!\n")
                print(f"Enemy Ships Left: {com_lives}\n")
        if com_lives == 0:
            print("All The ENEMY'S ships have been destroyed")
            print("You WIN !!!!!!!!!!!!!")
            should_continue = False
        # else:
        #     print("\n")
        #     print("Your missile missed the target . . .")
        #     print(f"Enemy Ships Left: {com_lives}\n")
        #     print("\n")

        return player_missile_x
        return player_missile_y


# --- COM MISSILE IS RANDOMLY GENERATED EACH ITERATION OF LOOP
def check_com_missile(enemy_missile_x, enemy_missile_y):
    '''
    FUNCTION: Generate random missile for computer
    '''
    global player_lives
    print("TIME FOR THE ENEMY TO FIRE AT YOU!\n")
    should_continue = True
    while should_continue:
        enemy_missile_x = random.sample(range(1, 6), 1)
        enemy_missile_y = random.sample(range(1, 6), 1)
        print(f"Enemy Missile Strike X: {enemy_missile_x}")
        print(f"Enemy Missile Strike Y: {enemy_missile_y}")
        print("\n")
        if player_position_x[0] == enemy_missile_x[0]:
            if player_position_y[0] == enemy_missile_y[0]:
                player_lives -= 1
                print("Your First Ship has been hit!!!\n")
                print(f"Player Ships Left: {player_lives}")
        if player_position_x[1] == enemy_missile_x[0]:
            if player_position_y[1] == enemy_missile_y[0]:
                player_lives -= 1
                print("Your Second Ship has been hit!!!\n")
                print(f"Player Ships Left: {player_lives}")
        if player_position_x[2] == enemy_missile_x[0]:
            if player_position_y[2] == enemy_missile_y[0]:
                player_lives -= 1
                print("Your Third Ship has been hit!!!\n")
                print(f"Player Ships Left: {player_lives}")
        if player_position_x[3] == enemy_missile_x[0]:
            if player_position_y[3] == enemy_missile_y[0]:
                player_lives -= 1
                print("Your Fourth Ship has been hit!!!\n")
                print(f"Player Ships Left: {player_lives}")
        if player_lives == 0:
            print("All your ships have been destroyed!!!")
            print("You Lose!!!")
            should_continue = False  
        # else:
        #     print("\n")
        #     print("ENEMY missile missed its target . . .")
        #     print(f"Player Ships Left: {player_lives}")
        #     print("\n")

        return enemy_missile_x
        return enemy_missile_y


def end_game():
    '''
    FUNCTION: Generate random missile for computer
    '''
    global com_lives
    global player_lives
    global game_over
    while not game_over:
        if com_lives >= 1 and player_lives >= 1:
            check_player_missile(player_missile_x, player_missile_y)
            check_com_missile(enemy_missile_x, enemy_missile_y)
        elif com_lives == 0:
            print("\n")
            print("GAME OVER: You Win!!!!!")
            game_over = True
        elif player_lives == 0:
            print("\n")
            print("GAME OVER: You lose")
            game_over = True


play_game()
rand_enemy_ships()
check_player_missile(player_missile_x, player_missile_y)
check_com_missile(enemy_missile_x, enemy_missile_y)
end_game()


# --------- BUGS AND SOURCES ------------- \\
'''https://www.codegrepper.com/code-examples/
python/how+to+generate+unique+random+numbers+in+python

BUG THAT ASKS FOR FIRST INPUT TWICE
i used None as a variable on player_missile variable to fix bug

https://stackoverflow.com/questions/11178061/
print-list-without-brackets-in-a-single-row

https://stackoverflow.com/questions/4435169
/how-do-i-append-one-string-to-another-in-python#comment88685663_4435169

https://stackoverflow.com/questions/28036309/
typeerror-list-object-cannot-be-interpreted-as-an-integer

https://stackoverflow.com/questions/18169965/
how-to-delete-last-item-in-list

https://www.codegrepper.com/code-examples/
python/how+to+generate+unique+random+numbers+in+python

check player missile ELSE statement doesn't work as intended
'''
