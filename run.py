from words import random_words
import time
import random


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


def get_random_word(random_word):
    """
    Generates a random word from the imported
    list of random words.
    """

    word = random.choice(random_words)
    return word.lower()


def main_game():
    """
    
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
    else:
        print(f'The word was {word}')
        print('You win :)')


def main():
    """
    
    """
    start_screen()
    main_game()


main()