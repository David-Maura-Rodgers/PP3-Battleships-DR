'''
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# TO RUN CODE: python3 run.py

# from random import randint

# import random
'''

# Player can place 4 ships at coordinates of their choosing
row1 = [".", ".", ".", ".", "."]
row2 = [".", ".", ".", ".", "."]
row3 = [".", ".", ".", ".", "."]
row4 = [".", ".", ".", ".", "."]
row5 = [".", ".", ".", ".", "."]

player_ships = []

player_board = [row1, row2, row3, row4, row5]

print("Please select where you want to place your ships\n")
print("The 1st number is the COLUMN, and the 2nd number is the ROW: \n")
print("Please only select from numbers 1 to 5\n")

# Player position input for ships
position_one = input("Please select number for COLUMN: \n")
position_two = input("Please select number for ROW \n")

# Convert both position inputs from string to integer
horizontal = int(position_one)
vertical = int(position_two)

# Updates board with the user input(postion variables) and places @ there.
# -1 used as the board starts at 0 for both column and rows: 0, 1, 2, 3, 4
player_board[vertical - 1][horizontal - 1] = "@"

# https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
print(' '.join(row1))
print(' '.join(row2))
print(' '.join(row3))
print(' '.join(row4))
print(' '.join(row5))