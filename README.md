# Hangman Game - Word Guessing Fun

This project is an interactive word game application that allows the user to play the classic game of Hangman against the computer. The application features two interfaces: one for the player and one for the administrator, providing a comprehensive gaming experience.

## Features

- **Player Interface:** The player interface allows users to play the Hangman game. They are given a certain number of guesses to correctly guess the secret word selected by the computer. The player receives feedback after each guess, revealing if the guessed letter is present in the secret word or not. The game ends when the player either guesses the word correctly or runs out of guesses.
- **Score Management:** The application keeps track of the player's score, which is calculated based on the number of guesses remaining multiplied by the number of unique letters in the secret word. The high score is also maintained, and a special message is displayed when a new high score is achieved.
- **Administrator Interface:** The administrator interface provides additional functionalities. The administrator can add new words to the word file, expanding the word pool for the game. They can also reset the highest score and the name of the player.

## Game Rules and Interface

- The application loads a list of available words from a file called `word.txt` at the start.
- Players start with a certain number of guesses and warnings.
- At the beginning of each game, the player is informed about the number of letters in the secret word, as well as the remaining guesses and warnings.
- The player enters one guess at a time, and the application provides feedback on whether the guessed letter is present in the secret word.
- The secret word is displayed to the player, with guessed letters revealed and unguessed letters displayed as underscores.
- Both uppercase and lowercase letters are accepted as valid guesses.
- The player loses a warning if they input anything other than alphabets or a letter that has already been guessed. If no warnings are left, the player loses a guess.
- If the player guesses a consonant that is not in the secret word, they lose one guess. If the guessed letter is a vowel not present in the secret word, they lose two guesses.
- The game ends when the player constructs the full word or runs out of guesses. If the player loses, the secret word is revealed. If the player wins, a congratulatory message is displayed along with the calculated score.
- The highest score achieved by a player is tracked and displayed, along with the player's name.

## Administrator Interface

The administrator interface provides the following functionalities:

- **Add New Words:** The administrator can add new words to the word file, expanding the available word pool for the game.
- **Reset Highest Score:** The administrator can reset the highest score and the name of the player.

## Getting Started

To run the Hangman game on your local machine, follow these steps:

1. Clone the repository to your local system.
2. Make sure you have Python installed.
3. Run the application using the command `python hangman.py`.
4. Follow the instructions on the screen to play the game or access the administrator interface.

## Contribution

Contributions to this project are welcome! If you have any ideas for improvements or bug fixes, feel free to submit a pull request. Let's make this Hangman game even more enjoyable!

Have fun playing Hangman!