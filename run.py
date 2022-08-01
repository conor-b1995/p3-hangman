from words import random_words
import time


def start_screen():
    """
    This is the opening visual for the user.
    It explains the rules and lets the user enter 
    there name. It also validates that the user entered
    only letters and not numbers into there name.
    """

    print('*' * 25)
    print('\nWelcome to the classic game of Hangman !!\n')
    print('*' * 25)
    time.sleep(1)

    print('The computer will generate a random word,\n\
you then have 6 attempts to guess each letter correctly \n\
or else an innocent man dies !!')
    time.sleep(3)

    while True:
        name = input('\nPlease enter your first name here: ')

        if validate_name(name):
            print(f'Good luck {name}')
            break


def validate_name(name):
    """
    Validates user data for name
    """
    try:
        if name == "":
            raise ValueError("Please input a name \n")
        elif not name.isalpha():
            raise ValueError("Use letters only.")

    except ValueError as error:
        print(f"Please try again. {error}")
        return False

    return True


start_screen()
