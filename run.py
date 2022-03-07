# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
print(f"You chose: ")
print(game_images[user_choice])

# STEPS TO CREATE RANDOM CHOICE FOR THE USER:
# Store the choices for the computer in the option list
# Create num_options variable using len on options list to convert to integer
# Pass in num_options to randint method to create the random number for the com_choice variable
# com_choice is created by using the options list and the random_choice varaible
options = [0, 1, 2]
num_options = len(options)
random_choice = random.randint(0, num_options - 1)
com_choice = options[random_choice]
print(f"Computer chose: ")
print(game_images[com_choice])


# ANGELA'S SOLUTION FOR RANDOM COMPUTER CHOICE
'''
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])
'''
print("\n")
print("---------- AND THE WINNER IS . . . . . . . \n")
print("\n")

# Condition for user choice - ROCK
if user_choice == 0 and com_choice == 1:
    print("PAPER BEATS ROCK!")
    print(paper)
    print(rock)
elif user_choice == 0 and com_choice == 2:
    print("ROCK BEATS SCISSORS!")
    print(rock)
    print(scissors)
elif user_choice == 0 and com_choice == 0:
    print("IT'S A DRAW!")

# Condition for user choice - PAPER
if user_choice == 1 and com_choice == 0:
    print("PAPER BEATS ROCK!")
    print(paper)
    print(rock)
elif user_choice == 1 and com_choice == 2:
    print("SCISSORS BEATS PAPER!")
    print(scissors)
    print(paper)
elif user_choice == 1 and com_choice == 1:
    print("IT'S A DRAW!")

# Condition for user choice - SCISSORS
if user_choice == 2 and com_choice == 0:
    print("ROCK BEATS SCISSORS!")
    print(rock)
    print(scissors)
elif user_choice == 2 and com_choice == 1:
    print("SCISSORS BEATS PAPER!")
    print(scissors)
    print(paper)
elif user_choice == 2 and com_choice == 2:
    print("IT'S A DRAW!")
