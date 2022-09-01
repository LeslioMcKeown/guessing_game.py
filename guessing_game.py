# Leslio McKeown
# 08/31/2022
""" Objections: Guess the number game, the players job is to make a guess, 
and you tell them whether their guess is too high or too low. Their next guess is 
based on what you've told them. If they guess the right answer the game is done.
"""
#Sources stackoverflow 
#Helper -- Roy 
#commented and edited some flaws in my previous attemps and made the new one similar to the example given 

import random

def validate_input_between(sentence: str, n: int):
    while True:
        try:
            number = int(input(f"{sentence} {n}: "))
            if 1 <= number <= n:
                return number
            raise ValueError()
        except ValueError:
            print(f"Input must be an integer between 1 and {n}.")


def start_game(n: int):
    guesses = 1
    random_number = random.randint(1, n)
    num = validate_input_between("Enter a number between 1 and", n)
    while True:
        if random_number > num:
           print("Your guess was too low.")
           num = validate_input_between("Guess another number between 1 and", n)
           guesses += 1
        elif random_number < num:
            print("Your guess was too high.")
            num = validate_input_between("Guess another number between 1 and", n)
            guesses += 1
        else:
            print("Good job! you guessed the right number!")
            print(f"The amount of guesses were {guesses}. \n Thanks for playing!!!  ^_^ ")
            break

start_game(10)