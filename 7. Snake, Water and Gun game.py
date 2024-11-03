'''
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where 
players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the
water beats the gun, and the snake beats the water. Write a python program to create a
Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI.
Use proper functions to check for win.
'''

import random 
op = ("snake","water","gun")

while True:
    bot = random.choice(op)

    user = input("Enter \'Snake\'\'/\'Water\'/\'Gun\' to play and 'q' to quit: ")
    if user.lower() == bot:
        print("Drawn!\n")

    elif user.lower() == 'snake' and bot == 'water':
        print("You Won!\n")

    elif user.lower() == 'snake' and bot == 'gun':
        print("Bot Won!\n")  

    elif user.lower() == 'water' and bot == 'snake' :
        print("Bot Won!\n")  

    elif user.lower() == 'water' and bot == 'gun':
        print("You Won/n")  

    elif user.lower() == 'gun' and bot == 'snake' :
        print("You Won!\n")  

    elif user.lower() == 'gun' and bot == 'water':
        print("Bot Won\n")           

    
    elif user.lower() == 'q':
        print("Thanks for Playing!")
        exit

    else:
        print("Wrong input!\n ")
