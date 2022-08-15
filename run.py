import os
import time
import random
from words import random_words


def start_screen():
    """
    This is the opening visual for the user.
    It lets the user enter there name.
    It also validates that the user has entered
    only letters and no numbers into there name.
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
        name = input('\nPlease enter your first name here: \n')

        if validate_name(name):
            print(f'Good luck {name}\n')
            break

    time.sleep(2)
    clear()
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
    print("\nThe computer will generate a random word,\n"
          "you then have 6 lives to guess each letter correctly.\n"
          "\nThe main objective of this game is to guess the word "
          "\nby choosing the correct letters, one at a time.\n"
          "\n1. To guess the word, type a letter of your choice "
          "\nthen press the enter key. \n"
          "\n2. If your selection is correct "
          "\nthe letter will be displayed on the screen. \n"
          "\n3. If the letter selected is wrong, the hangman figure "
          "\nwill start to appear on the screen and you will lose a life. \n"
          "\n4. You are given 6 lives before the game is over. \n"
          "\n5. If you get stuck running the game please click on "
          "\nRUN PROGRAM at the top of the screen, "
          "to reset the game. \n\n")
    menu()


def menu():
    """
    This is the menu to give users options between
    reading the intructions or playing the game.
    """
    print('Main Menu')
    print('1. Instructions\n2. Play Game\n')

    while True:
        pick_number = input('Please select an option: \n')

        if pick_number == '1':
            clear()
            instructions()
            break
        elif pick_number == '2':
            clear()
            main_game()
            break
        else:
            print('Invalid input please enter "1" or "2"')


def get_random_word():
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
    word = get_random_word()
    letters_in_word = set(word)

    while len(letters_in_word) > 0 and lives > 0:

        display_answer_grid = [
            letter if letter in guessed_letters else '_' for letter in word]

        # print('\nLetters guessed: ', ','.join(guessed_letters))
        print(hangman_figure(lives))
        print(f'{lives} live(s) remaining !\n')
        print('Current word: ', " ".join(display_answer_grid))
        player_guess = input('\nGuess a letter: \n').lower()
        print('\n')

        clear()

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
            print(f'{player_guess} is not in the word')
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
        print(hangman_figure(lives))
        print('Sorry you lost')
        print(f'The word was {word}\n')
        another_game()
    else:
        print('You win :)')
        print(f'The word was {word}\n')
        another_game()


def another_game():
    """
    Gives the user the option to play
    another game or to just exit the
    game.
    """
    while True:
        play_again = input('Would you like to play another game ?\
    yes/no\n').lower()

        if play_again == 'yes':
            main_game()
        elif play_again == 'no':
            print('Game over ! Press "Run Program" if you want to play again')
            exit()
        else:
            print('Please make a valid choice !!')


def hangman_figure(lives):
    """
    The different stages of hangman
    depending on how many lives the
    user has left.
    """

    steps = [  # sixth stage
          """
             --------
             |      |
             |      O
             |     \\|/
             |      |
             |     / \\
             -
          """,
          # fifth stage
          """
             --------
             |      |
             |      O
             |     \\|/
             |      |
             |     /
             -
          """,
          # fourth stage
          """
             --------
             |      |
             |      O
             |     \\|/
             |      |
             |
             -
          """,
          # third stage
          """
             --------
             |      |
             |      O
             |     \\|
             |      |
             |
             -
          """,
          # second stage
          """
             --------
             |      |
             |      O
             |      |
             |      |
             |
             -
          """,
          # first stage
          """
             --------
             |      |
             |      O
             |
             |
             |
             -
          """,
          # Initial stage
          """
             --------
             |      |
             |
             |
             |
             |
             -
          """
    ]

    return steps[lives]


def clear():
    """
    Used to clear terminal of clutter.
    """
    os.system('clear')


def main():
    """
    Main function that takes in the
    other functions to run the game.
    """
    start_screen()
    main_game()


main()
