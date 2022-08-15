# Hangman
Traditionally hangman is a guessing game for two or more players. One player thinks of a word or phrase and the other(s) tries to guess it by suggesting letters within a certain number of guesses.

My version of the game allows only one user at a time to play. The computer will randomly pick a word from a predefined list of words. The random word will then be displayed with '_' for each letter in the random word. Then the user can try to guess the word by inputting letters, if the letter is wrong a visual of the hangman man will start to appear, if the letter is in the word the letter appears and another guess can be made. The user can keep guessing letters until either all 6 lives are used or the user has successfully guessed all the correct letters. The aim is to supply a fun word guessing game to the user.
(Responsive image)

## User Experience(UX)
### User goals
* A nice welcome screen which lets the user interact with the game immediately.
* The game menu is very clear and user-friendly.
* The instructions are easily read and easily understood by the user.
* The game itself is very clear and easy to interact with.

## Features
### Start Screen
* The start screen welcomes the user to the game.
* It also lets the user input their first name and the game wishes the user good luck
(Start screen image)
### Main menu
* The main menu allows the user to check out the instructions for the game.
* The user also enters the main game from the main menu by inputting the corresponding number. 
(Menu image)
### Instructions
* The instructions section clearly outlines how the game works for the user.
* The main menu comes up here again so the user can continue to the main game.
(Instructions image)
### Main Game
* In the main game the user will be able to see: 
    * The letter they have just selected and whether or not it is in the word.
    * All the previous letters they have used.
    * The stages of the hangman figure.
    * How many lives they have remaining.
    * The current word they are trying to guess.
    * The user will be given the option to play again after they have won or lost.
    * Game will exit if the user selects 'no'.


### Future Features
* A possible future idea is to make it two player, so player one can type in any word of their choice the word will then be hidden and player two will have to guess the word.
* Making the game different levels so a group of easy words, medium words and hard words to accommodate all skill levels. 
* Adding a timer to the game to make it more difficult. 

## Testing
* Throughout my project I used the gitpod terminal to run and test that each function was working correctly as I was creating the functions.
* I got some of my friends to test the game to make sure the game was running smoothly. Although the game ran smoothly for them they found a lot of the words very tricky so I changed my list.
* ### Validator testing
    * I ran my code through the [PEP8 Validator](http://pep8online.com/) with no issues.
(Validation image)

## Bugs
* While doing the another_game function the else statement was just printing out an infinite amount of the string. This bug was fixed by surrounding it in a while loop.

## Deployment



## Credits
