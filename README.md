# Russian-Gameland-Application

This is a word game application that includes three word-based games: Wordle, Hangman, and Unscrambler. The application is built using the tkinter library in Python. The games are designed to be played with a Russian keyboard layout.

# Game Descriptions
### Wordle

Wordle is a game where the player tries to guess a five-letter word within a certain number of allowed guesses. The player enters a guess in the form of a five-letter word, and the application provides feedback on the correctness of the guess. The game ends when the player either guesses the word correctly or uses up all the allowed guesses.

### Hangman

Hangman is a classic word-guessing game. The player tries to guess a secret word by suggesting letters. The game provides feedback on the correctness of the guesses and displays a hangman ASCII art that represents the number of missed guesses. The player wins if they guess the word correctly or loses if they reach the maximum number of allowed missed guesses.

### Unscrambler

Unscrambler is a game where the player tries to unscramble a given word. The application shuffles the letters of a secret word and presents the player with the scrambled word. The player needs to guess the original word by rearranging the letters. The player has a limited number of guesses, and the game ends when they either unscramble the word correctly or use up all the allowed guesses.

# Usage

To run the game, execute the Python script GUI.py. The application will display a graphical user interface (GUI) with a menu where you can select one of the available games. After choosing a game, follow the instructions on the screen to play the selected game.
##### Note: These games are designed to be played with a Russian keyboard layout. Please ensure that your keyboard is set to the Russian layout before playing the games.

# Customization

The games can be customized by adding new word themes or modifying the existing themes. The word themes are defined in the words.py file. Simply add new word lists or modify the existing ones to suit your preferences or language

# Prerequisites

To run the application, you need to have Python installed on your system. The application uses the tkinter library, which is included in the standard Python library.

# Files

The application consists of the following files:

    GUI.py: The main script to run the application.
    words.py: A Python file that contains word lists for different themes used in the games.
    README.md (this file): A readme file that provides information about the application.

# Dependencies

The application has the following dependencies:

    Python 3.x
    tkinter library (included in Python standard library)

# License

The source code of this application is released under the MIT License. You can find the details in the LICENSE file.

# Acknowledgements

This application was created by John Jones.
