# %%
import random # Import the random module to choose a random word from the list of words
WORDS = [
    "python", "computer", "hangman", "keyboard", "program", #   First five words
    "developer", "variable", "function", "terminal", "internet" #   Last five words
]
HANGMAN_PICS = [
    " +---+\n |   |\n     |\n     |\n     |\n     |\n=========", #First element is the empty gallows 
    " +---+\n |   |\n O   |\n     |\n     |\n     |\n=========", #Second element is the head
    " +---+\n |   |\n O   |\n |   |\n     |\n     |\n=========", #Third element is the body
    " +---+\n |   |\n O   |\n/|   |\n     |\n     |\n=========", #Fourth element is the left arm
    " +---+\n |   |\n O   |\n/|\  |\n     |\n     |\n=========", #Fifth element is the right arm
    " +---+\n |   |\n O   |\n/|\  |\n/    |\n     |\n=========", #Sixth element is the left leg
    " +---+\n |   |\n O   |\n/|\  |\n/ \  |\n     |\n=========" #Seventh element is the right leg
]
#now we need to choose a random word from the list of words. We will create a function that will return a random word from the list of words.
def choose_word(): # Function to choose a random word from the list of words
    return random.choice(WORDS) # Return a random word from the WORDS list
# now we need to display the current state of the word with guessed letters and underscores for unguessed letters. We will create a function that will take the secret word and the guessed letters as input and return a string with the current state of the word.
def display_word(secret_word, guessed_letters): # Function to display the current state of the word with guessed letters and underscores for unguessed letters
    shown_word = "" # Initialize an empty string to hold the displayed word
    for letter in secret_word: # Loop through each letter in the secret word
        if letter in guessed_letters: # If the letter has been guessed, add it to the displayed word
            shown_word += letter + " " # Add the guessed letter followed by a space(for presentation purpose)
        else: # If the letter has not been guessed, add an underscore to the displayed word
            shown_word += "_ " # Add an underscore followed by a space(for presentation purpose)
    return shown_word # Return the displayed word with guessed letters and underscores for unguessed letters
# Now we need to get a guess from the player. We will create a function that will ask the player for a guess and check if it is valid. If it is not valid, we will ask the player to enter a new guess until they enter a valid guess. We will also check if the guess has already been guessed. If it has, we will ask the player to enter a new guess until they enter a valid guess.
def get_guess(guessed_letters): # Function to get a valid guess from the player
    while True:
        print()
        print("Guessed so far:", " ".join(guessed_letters)) # Print the letters that have been guessed so far, joined by spaces
        guess = input("Enter ONE new letter: ").lower().strip() # Get the player's guess, convert it to lowercase, and remove any leading or trailing whitespace
        print("You typed:", guess) # Print the player's guess for confirmation
# Now we need to see if the input is valid. We will check if the input is a single letter, if it is a letter, and if it has already been guessed.
        if len(guess) != 1:
            print("Please enter only one letter, for example: e")
        elif not guess.isalpha(): # Check if the guess is a letter (not a number or symbol)
            print("Please enter a letter from A to Z.")
        elif guess in guessed_letters:
            print("You already guessed that letter.") # Check if the letter has already been guessed
        else:
            return guess
#now we need to check if the player has guessed all the letters in the secret word. We will create a function that will take the secret word and the guessed letters as input and return True if the player has guessed all the letters in the secret word, and False otherwise.
def check_win(secret_word, guessed_letters): # Function to check if the player has guessed all the letters in the secret word
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True
#now we need to play the game of Hangman. We will create a function that will play the game of Hangman. We will use a while loop to keep asking the player for guesses until they win or lose. We will also keep track of the number of wrong guesses and display the current state of the hangman drawing based on the number of wrong guesses.
def play_game(): # Function to play the game of Hangman
    secret_word = choose_word()
    guessed_letters = []
    wrong_guesses = 0 # Initialize the number of wrong guesses to 0
    max_wrong = len(HANGMAN_PICS) - 1 # Set the maximum number of wrong guesses to the length of the HANGMAN_PICS list minus 1 (since the first element is the empty gallows)

    print("Welcome to Hangman!")
    print("Guess the word before the man is fully drawn.")

    while True: # Loop until the player wins or loses
        print(HANGMAN_PICS[wrong_guesses]) # Print the current state of the hangman drawing based on the number of wrong guesses
        print("Word:", display_word(secret_word, guessed_letters))
        #print("Guessed letters:", " ".join(guessed_letters))
        print("Wrong guesses:", wrong_guesses, "/", max_wrong)
        print()

        if check_win(secret_word, guessed_letters):
            print("You win!")
            print("The word was:", secret_word)
            break

        if wrong_guesses >= max_wrong:
            print("You lose!")
            print("The word was:", secret_word)
            break

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            wrong_guesses += 1
        print("-" * 30) # Print a separator line for better readability
#now we need to ask the player if they want to play again. We will create a function that will ask the player if they want to play again and return True if they do, and False otherwise.
def Start(): # Function to start the game and ask the player if they want to play again
    while True:
        play_game()

        again = input("Play again? y/n: ").lower().strip()

        if again != "y":
            print("Thanks for playing!")
            break
Start()

# %%
