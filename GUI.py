import tkinter as tk
from tkinter import messagebox
from words import word_list
from words import одежда, дом, семья, еда, школа
import random

hangBoard = [
    """
   +---+
   |   |
       |
       |
       |
       |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]
#Colors for wordle
dark_grey = "#777b7d"
yellow = "#c9b458"
green = "#6aaa64"

#Total guesses for wordle
ALLOWED_GUESSES = 6

#Multi Use Functions
def getRandomWord(theme): 
    """Randomly chooses a word from selected theme and returns word list

    Args:
        theme (string): The theme selected from userInput
    
    Returns"
        list: The selected theme from the words.py file
    """
    themes = {'одежда': одежда, 'школа': школа, 'дом': дом, 'семья': семья, 'еда': еда}
    return random.choice(themes[theme])

def on_button_click(event): #Used to wait until action happens i.e. Enter key or button clicked
    variable.set(True)  # Set the variable to True when the button is clicked

def wait_for_button(guess_entry):
    """Waits for <Return> to be pressed

    Args:
        guess_entry (tk.Entry object): The entry where the data will come from
    
    Returns:
        string: The data in the entry object
    """
    guess_entry.wait_variable(variable) 
    return guess_entry.get().lower()

def play_again(game_frame, main_frame): 
    """
    Used to return to theme selection for certain games
    
    Args: 
        game_frame (tk.Frame object): The frame where the game is played
        main_frame (tk.Frame object): The frame where the theme is selected for most game
    """
    play_again = messagebox.askquestion("Play Again", "Do you want to play again?")
    if play_again == 'yes':
        game_frame.pack_forget()
        main_frame.pack()
    else:
        show_menu_frame()

def w_play_again():
    """
    Used to play wordle again and clear the label objects
    """
    play_again = messagebox.askquestion("Play Again", "Do you want to play again?")
    if play_again == 'yes':
        clear_wordle()
        wordle_start_game()
    else:
        clear_wordle()
        show_menu_frame()

#Wordle Functions
def clear_wordle():
    """
    Used to clear the wordle button objects from the frame
    """
    for label in full_wordle_pattern:
        label.destroy()

def correct_place(form, letter, row, col):
    """
    Create and place a label in a form at the specified row and column. Used for letter in the word and in the right place

    Args:
        form (tkinter.Tk): The form to place the label in.
        letter (str): The text to be displayed on the label.
        row (int): The row index in the form where the label should be placed.
        col (int): The column index in the form where the label should be placed.

    Returns:
        tkinter.Label: The created label widget colored green
    """
    label = tk.Label(
            form,
            font=("Arial", 10, "bold"),
            text=letter,
            width=8,
            height=4,
            borderwidth=1,
            relief="ridge",
            anchor="center",
            bg=green)
    label.grid(row=row, column=col,padx=1,pady=1)
    return label
def correct_letter(form, letter,row, col):
    """
    Create and place a label in a form at the specified row and column. Used for letter in the word but not in the right place

    Args:
        form (tkinter.Tk): The form to place the label in.
        letter (str): The text to be displayed on the label.
        row (int): The row index in the form where the label should be placed.
        col (int): The column index in the form where the label should be placed.

    Returns:
        tkinter.Label: The created label widget colored yellow
    """
    label = tk.Label(
            form,
            font=("Arial", 10, "bold"),
            text=letter,
            width=8,
            height=4,
            borderwidth=1,
            relief="ridge",
            anchor="center",
            bg=yellow)
    label.grid(row=row, column=col,padx=1,pady=1)
    return label
def incorrect_letter(form, letter, row, col):
    """
    Create and place a label in a form at the specified row and column. Used for letter not in the word

    Args:
        form (tkinter.Tk): The form to place the label in.
        letter (str): The text to be displayed on the label.
        row (int): The row index in the form where the label should be placed.
        col (int): The column index in the form where the label should be placed.

    Returns:
        tkinter.Label: The created label widget colored dark_gray
    """
    label = tk.Label(
            form,
            font=("Arial", 10, "bold"),
            text=letter,
            width=8,
            height=4,
            borderwidth=1,
            relief="ridge",
            anchor="center",
            bg=dark_grey)
    label.grid(row=row, column=col,padx=1,pady=1)
    return label
    
def check_guess(guess, answer,r):
    """
    Goes through each letter in guess and checks against answer and places label

    Args:
        guess (str): The str taken from the tk.Entry
        answer (str): The answer to check against guess
        r (int): The current row to place the guess

    Returns:
        wordle_pattern (list): Current list of all tk.Label objects

    """
    wordle_pattern = []
    row = r
    col = 0
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            label = correct_place(wordle_form, letter, row, col)
            wordle_pattern.append(label)
            col+=1
        elif letter in answer:
            label = correct_letter(wordle_form, letter, row, col)
            wordle_pattern.append(label)
            col+=1
        else:
            label = incorrect_letter(wordle_form, letter, row, col)
            wordle_pattern.append(label)
            col+=1
    return wordle_pattern

def wordle_game(chosen_word):
    """
    Runs the full Wordle game with the specified chosen word.

    Args:
        chosen_word (str): The randomly chosen word from the theme selection.

    """
    global full_wordle_pattern
    
    #Initialize game variables
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []
    row = 3
    
    while not end_of_game:

        # Waits for players guess
        guess = wait_for_button(wordle_guess_entry).upper()

        while guess == '':
            guess = wait_for_button(wordle_guess_entry).upper()

        while len(guess) != 5 or guess in already_guessed or guess.lower() not in word_list:
            # Check for invalid guesses and show appropriate message
            if guess in already_guessed:
                messagebox.showinfo("Try again","Вы уже угадали это слово!!")
            elif guess.lower() not in word_list:
                messagebox.showinfo("Try again","Word not in word list. Try again.")
            else:
                messagebox.showinfo("Try again",'Пожалуйста, введите слово из 5 букв!!')
            
            # Prompt for a new guess
            guess = wait_for_button(wordle_guess_entry).upper()
        
        already_guessed.append(guess)
        pattern = check_guess(guess, chosen_word,row)
        all_words_guessed.append(guess)

        for label in pattern:
            full_wordle_pattern.append(label)
        
        # Check if game is over
        if guess == chosen_word or len(already_guessed) == ALLOWED_GUESSES:
            end_of_game = True
        
        row+=1
        wordle_guess_entry.delete(0, tk.END)
    
    # Show game outcome
    if len(already_guessed) == ALLOWED_GUESSES and guess != chosen_word:
        messagebox.showinfo("You lost",f"\nВОРДЛИ X/{ALLOWED_GUESSES}\nПравильное слово: {chosen_word}")
    else:
        messagebox.showinfo("Congrats",f"\nВОРДЛИ {len(already_guessed)}/{ALLOWED_GUESSES}\n")
    
    # Prompt to play
    w_play_again()

#Hangman Functions
def displayBoard(hang, missedLetters, correctLetters, secretWord):
    """
    Updates the display of the hangman game board based on the game state.

    Args:
        hang (list): List of hangman ASCII art corresponding to the number of missed letters.
        missedLetters (list): List of missed letters.
        correctLetters (list): List of correctly guessed letters.
        secretWord (str): The secret word to be guessed.

    """
    # Update hangman ASCII art display
    hangman_text.config(text=hang[len(missedLetters)])

    # Update missed letters display
    hangman_missed_letters_text.config(text='Неправильные буквы: ' + ' '.join(missedLetters))

    # Creates blanks for secret word
    blanks = '_' * len(secretWord)

    # Replace blanks with correctly guessed letters
    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    # Update the secret word display
    hangman_secret_word_text.config(text=' '.join(blanks))

def getGuess(alreadyGuessed):
    """
    Retrieves a valid guess from the player.

    Args:
        alreadyGuessed (list): List of letters already guessed by the player.

    Returns:
        guess (str): The valid guess entered by the player.

    """
    hangman_guess_entry.delete(0, tk.END)
    while True:
        # Wait for guess
        guess = wait_for_button(hangman_guess_entry)
        
        # Don't allow empty guesses
        while guess == '':
            guess = wait_for_button(hangman_guess_entry)
        
        # Check for invalid guesses and show appropriate message
        if len(guess) > 1:
            # Invalid guess: More than one letter entered
            messagebox.showinfo("Invalid Guess", "Please enter only one letter.")
            hangman_guess_entry.delete(0, tk.END)
        elif guess in alreadyGuessed:
            # Invalid guess: Letter already guessed
            messagebox.showinfo("Invalid Guess", "You have already guessed that letter.")
            hangman_guess_entry.delete(0, tk.END)
        elif guess not in 'йцукенгшщзхъфывапролджэячсмитьбюё':
            # Invalid guess: Non-alphabetic character entered
            messagebox.showinfo("Invalid Guess", "Please enter a Russian letter.")
            hangman_guess_entry.delete(0, tk.END)
        else:
            break

    return guess

def hangman_game(secretWord):
    """
    Runs the hangman game with the given secret word.

    Args:
        secretWord (str): The secret word to be guessed.

    """
    # Initialize game variables
    missedLetters = ''
    correctLetters = ''
    gameIsDone = False
    hangman_guess_entry.delete(0, tk.END)

    while True:
        displayBoard(hangBoard, missedLetters, correctLetters, secretWord)
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess
            foundAllLetters = True

            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                messagebox.showinfo("Congratulations", "Да! Секретное слово - это: \"" + secretWord + "\"")
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            if len(missedLetters) == len(hangBoard) - 1:
                displayBoard(hangBoard, missedLetters, correctLetters, secretWord)
                messagebox.showinfo("Game Over", "Ты проиграл!!\nСекретное слово - это: " + secretWord)
                gameIsDone = True

        if gameIsDone:
            play_again(hangman_game_frame, hangman_main_frame)

#Unscrambler Functions
def shuffle_word(randomWord):
    """
    Shuffles the letters of a word randomly.

    Args:
        randomWord (str): The word to be shuffled.

    Returns:
        str: The shuffled word.

    """
    word = list(randomWord)
    random.shuffle(word)
    return ''.join(word)

def unscrambler_game(secretWord):
    """
    Runs the unscrambler game where the player tries to unscramble a word.

    Args:
        secretWord (str): The secret word to be unscrambled.

    """
    guesses = 0
    MAX_GUESS = 3

    # Shuffle the letters of the secret word and display
    scr_word = shuffle_word(secretWord)
    unscrambler_scrambled_word_label.config(text=' '.join(scr_word))
    
    while True:
        guess = wait_for_button(unscrambler_guess_entry)
        
        # Don't allow empty guesses
        while guess == '':
            guess = wait_for_button(unscrambler_guess_entry)

        if guess == secretWord:
            # Player has successfully unscrambled the word
            messagebox.showinfo("Good job!",f"Congratulations! '{guess}' was the secret word!\n")
            play_again(unscrambler_game_frame, unscrambler_main_frame)

        elif guesses == MAX_GUESS:
            # Player has used all the guesses and failed
            messagebox.showinfo("You lost",'You have used all the guesses\n\nYou have lost!\nСекретное слово - это: "' + secretWord)
            play_again(unscrambler_game_frame, unscrambler_main_frame)
        else:
            # Player isn't correct and hasn't used all guesses
            guesses+=1
            if guesses < MAX_GUESS:
                # Player's guess is incorrect but has more chances left
                messagebox.showinfo("Try again!",f'"{guess}" is not correct. Try again! {guesses}/{MAX_GUESS}')
                unscrambler_guess_entry.delete(0, tk.END)
            else:
                # Player's guess is incorrect and it's their last chance
                messagebox.showinfo("Try again!",f'"{guess}" is not correct. Last TRY!')
                unscrambler_guess_entry.delete(0, tk.END)

#Main Menu Functions
def show_menu_frame():
    """
    Displays the menu frame and hides other frames.
    """
    hangman_main_frame.pack_forget()
    hangman_game_frame.pack_forget()
    unscrambler_main_frame.pack_forget()
    unscrambler_game_frame.pack_forget()
    wordle_game_frame.pack_forget()
    wordle_form.pack_forget()
    menu_frame.pack()

def show_frame(showFrame):
    """
    Displays the specified frame and hides the menu frame.

    Args:
        showFrame (tk.Frame): The frame to be displayed.
    """
    menu_frame.pack_forget()
    showFrame.pack()

def launch_wordle():
    """
    Launches the wordle game.
    """
    show_frame(wordle_game_frame)
    wordle_start_game()

def launch_unscrambler():
    """
    Launches the unscrambler game.
    """
    show_frame(unscrambler_main_frame)

def launch_hangman():
    """
    Launches the hangman game.
    """
    show_frame(hangman_main_frame)

def go_back():
    """
    Goes back to the menu frame and clears any ongoing game state.
    """
    try:
        clear_wordle()
    finally:
        show_menu_frame()

window = tk.Tk()
window.title("Russian Gameland")
window.geometry("500x600")
window.resizable(False,False)

# Main Menu
menu_frame = tk.Frame(window)
back_btn = tk.Button(window, text="Back", command=go_back,bg='red')
back_btn.pack(pady=10)
back_btn.place(x=0,y=575)

# Welcome labels and information
welcome_label = tk.Label(menu_frame, text="Welcome to Russian Gameland", font=("Arial", 20),foreground="blue")
welcome_label.pack(pady=20)
information_label = tk.Label(window, text="Created by: John Jones", font=("Arial", 10),fg="blue")
information_label.pack(pady=20)
information_label.place(x=360,y=575)   

# Game buttons
wordle_btn = tk.Button(menu_frame, text="Wordle", command=launch_wordle)
wordle_btn.pack(pady=10)
unscrambler_btn = tk.Button(menu_frame, text="Unscrambler", command=launch_unscrambler)
unscrambler_btn.pack(pady=10)
hangman_btn = tk.Button(menu_frame, text="Hangman", command=launch_hangman)
hangman_btn.pack(pady=10)

#Back button
back_btn = tk.Button(window,text="Back",command=go_back)

menu_frame.pack()

#Wordle Frame
#######################################################################
wordle_game_frame = tk.Frame(window)
wordle_game_frame.pack_forget()
wordle_form = tk.Frame(window)
wordle_form.pack_forget()

wordle_welcome_label = tk.Label(wordle_game_frame, text="Russian Wordle:", font=("Arial", 25),foreground='blue')
wordle_guess_label = tk.Label(wordle_game_frame, text="Guess a word:", font=("Arial", 12))
wordle_guess_label.grid(row=1, column=0,padx=1,pady=1)
wordle_welcome_label.grid(row=0,column=0,padx=1,pady=1)

wordle_guess_entry = tk.Entry(wordle_game_frame, font=("Arial", 12))
wordle_guess_entry.grid(row=2, column=0,padx=1,pady=1)
wordle_guess_entry.bind("<Return>",on_button_click)

def wordle_start_game():
    """
    Starts the Wordle game by choosing a random word and displaying the game frame.
    """
    chosen_word = random.choice(word_list).upper()
    wordle_game_frame.pack()
    wordle_form.pack()
    wordle_game(chosen_word)

#Hangman Frame
#######################################################################
hangman_main_frame = tk.Frame(window)
hangman_main_frame.pack_forget()

#Pick a theme
hangman_theme_label = tk.Label(hangman_main_frame, text="Тема?", font=("Arial", 16))
hangman_theme_label.pack(pady=20)

hangman_theme_options = ['одежда', 'школа', 'дом', 'семья', 'еда']
hangman_theme_var = tk.StringVar(hangman_main_frame)
hangman_theme_var.set(hangman_theme_options[0])

hangman_theme_menu = tk.OptionMenu(hangman_main_frame, hangman_theme_var, *hangman_theme_options)
hangman_theme_menu.pack(pady=10)

#Plays game
hangman_play_button = tk.Button(hangman_main_frame, text="Play",command=lambda: hangman_start_game(hangman_theme_var.get()))
hangman_play_button.pack(pady=10)

#Actual game
hangman_game_frame = tk.Frame(window)

hangman_game_frame.pack_forget()

hangman_text = tk.Label(hangman_game_frame, text="", font=("Courier", 14), pady=20)
hangman_text.pack()

hangman_missed_letters_text = tk.Label(hangman_game_frame, text="", font=("Arial", 12))
hangman_missed_letters_text.pack(pady=10)

hangman_secret_word_text = tk.Label(hangman_game_frame, text="", font=("Arial", 16))
hangman_secret_word_text.pack(pady=10)

hangman_guess_label = tk.Label(hangman_game_frame, text="Угадай букву:", font=("Arial", 12))
hangman_guess_label.pack()

hangman_guess_entry = tk.Entry(hangman_game_frame, font=("Arial", 12))
hangman_guess_entry.pack(pady=10)
hangman_guess_entry.bind("<Return>",on_button_click)

variable = tk.BooleanVar()
variable.set(False)

def hangman_start_game(theme):
    """
    Starts the Hangman game by choosing a secret word based on the selected theme and displaying the game frame.

    Args:
        theme (str): The selected theme for the game.
    """
    secretWord = getRandomWord(theme)
    hangman_game_frame.pack()
    hangman_main_frame.pack_forget()
    hangman_game(secretWord)
#######################################################################

#Unscrambler Frame
unscrambler_main_frame = tk.Frame(window)
unscrambler_main_frame.pack_forget()

#Pick a theme
unscrambler_theme_label = tk.Label(unscrambler_main_frame, text="Тема?", font=("Arial", 16))
unscrambler_theme_label.pack(pady=20)

unscrambler_theme_options = ['одежда', 'школа', 'дом', 'семья', 'еда']
unscrambler_theme_var = tk.StringVar(unscrambler_main_frame)
unscrambler_theme_var.set(unscrambler_theme_options[0])

unscrambler_theme_menu = tk.OptionMenu(unscrambler_main_frame, unscrambler_theme_var, *unscrambler_theme_options)
unscrambler_theme_menu.pack(pady=10)

unscrambler_play_button = tk.Button(unscrambler_main_frame, text="Play",command=lambda: unscrambler_start_game(unscrambler_theme_var.get()))
unscrambler_play_button.pack(pady=10)

#Unscrambler Game
unscrambler_game_frame = tk.Frame(window)
unscrambler_game_frame.pack_forget()

unscrambler_text = tk.Label(unscrambler_game_frame, text="", font=("Courier", 14), pady=20)
unscrambler_text.pack()

unscrambler_scrambled_word_label = tk.Label(unscrambler_game_frame, text="", font=("Arial", 12))
unscrambler_scrambled_word_label.pack(pady=10)

unscrambler_guess_label = tk.Label(unscrambler_game_frame, text="Unscramble the word above:", font=("Arial", 12))
unscrambler_guess_label.pack()

unscrambler_guess_entry = tk.Entry(unscrambler_game_frame, font=("Arial", 12))
unscrambler_guess_entry.pack(pady=10)
unscrambler_guess_entry.bind("<Return>",on_button_click)

variable = tk.BooleanVar()
variable.set(False)

def unscrambler_start_game(theme):
    """
    Starts the Unscrambler game by choosing a scrambled word based on the selected theme and displaying the game frame.

    Args:
        theme (str): The selected theme for the game.
    """
    unscrambler_guess_entry.delete(0,tk.END)
    secretWord = getRandomWord(theme)
    unscrambler_game_frame.pack()
    unscrambler_main_frame.pack_forget()
    unscrambler_game(secretWord)

window.mainloop()