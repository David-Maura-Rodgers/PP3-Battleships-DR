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


player_board = [row1, row2, row3, row4, row5]
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n")

# The 1st number 'position_one' is the COLUMN, and the 2nd number
# 'position_two' is the ROW: "
print("Please only select from numbers 1 to 5\n")

# print("The 1st number 'position_one' is the COLUMN,
# and the 2nd number 'position_two' is the ROW: \n")

position_one = input("Please select number for COLUMN: \n")
position_two = input("Please select number for ROW \n")

# Example input: "23"
# Horizontal is the first number for COLUMN: This code gets the first
# number "2" as its Index is [0]
# Vertical is the second number "3" for the ROW: This code gets the second
# number as its Index is [1]

# convert the position input from string to integer
horizontal = int(position_one)
vertical = int(position_two)

# updates map with the user input(postion variable) and places X there.
# -1 used as the map starts at 0 for both column and rows: 0, 1, 2
player_board[vertical - 1][horizontal - 1] = "@"


# print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")

# https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
print(' '.join(row1))
print(' '.join(row2))
print(' '.join(row3))
print(' '.join(row4))
print(' '.join(row5))

# print(player_board[vertical -1])
