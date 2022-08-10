import time
import random
from words import random_words


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

#     print('The computer will generate a random word,\n\
# you then have 6 attempts to guess each letter correctly \n\
# or else an innocent man dies !!')
    # time.sleep(3)

    while True:
        name = input('\nPlease enter your first name here: ')

        if validate_name(name):
            print(f'Good luck {name}')
            break

    menu()


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


def instructions():
    """
    Instructions so thr user can understand
    how the game works.
    """
    print('The computer will generate a random word,\n\
you then have 6 attempts to guess each letter correctly \n\
or else an innocent man dies !!\n')
    menu()


def menu():
    """
    This is the menu to give users options between
    reading the intructions or playing the game.
    """
    print('1. Instructions\n2. Play Game\n')

    while True:
        pick_number = input('Please select an option: \n')

        if pick_number == '1':
            instructions()
            break
        elif pick_number == '2':
            main_game()
            break
        else:
            print('Invalid input please enter "1" or "2"')


def get_random_word(random_word):
    """
    Generates a random word from the imported
    list of random words.
    """

    word = random.choice(random_words)
    return word.lower()


def main_game():
    """
    Main function to grab a random word from
    get_random_word function which is then hidden
    so the user cant see the random word. Takes user
    input and validates it. Decrement user life when
    the letter they guess isnt in the random word.
    """
    lives = 6
    guessed_letters = []
    word = get_random_word(random_words)
    letters_in_word = set(word)

    while len(letters_in_word) > 0 and lives > 0:

        display_answer_grid = [letter if letter in guessed_letters else '_' for letter in word]

        # print('\nLetters guessed: ', ','.join(guessed_letters))
        print(f'{lives} lives remaining !\n')
        print('Current word: ', " ".join(display_answer_grid))
        player_guess = input('Guess a letter: ').lower()
        print('\n')

        if player_guess in guessed_letters:
            print(f'Sorry you have already guessed {player_guess}')
            print('You have used these letters: ', ','.join(guessed_letters))

        elif not player_guess.isalpha():
            print(f'{player_guess} is not a letter. Only enter letters.')
            print('You have used these letters: ', ','.join(guessed_letters))

        elif len(player_guess) != 1:
            print('You must only use one single letter !!')
            print('You have used these letters: ', ','.join(guessed_letters))

        elif player_guess not in word:
            print(f'Please try again {player_guess} is not in the word')
            lives -= 1
            # print(f'{lives} lives remaining')
            guessed_letters.append(player_guess)
            print('You have used these letters: ', ','.join(guessed_letters))

        else:
            print(f'Good job! {player_guess} is in the word \n')
            guessed_letters.append(player_guess)
            print('You have used these letters: ', ','.join(guessed_letters))
            if player_guess in letters_in_word:
                letters_in_word.remove(player_guess)

    if lives == 0:
        print('Sorry you lost')
        print(f'The word was {word}')
        exit()
    else:
        print(f'The word was {word}')
        print('You win :)')
        exit()


def main():
    """
    Main function that takes in the
    other functions to run the game.
    """
    start_screen()
    main_game()


main()
