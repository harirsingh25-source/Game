# %%
import random

WORDS = [
    "python", "computer", "hangman", "keyboard", "program",
    "developer", "variable", "function", "terminal", "internet"
]

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def choose_word():
    return random.choice(WORDS)

def display_word(secret_word, guessed_letters):
    shown_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            shown_word += letter + " "
        else:
            shown_word += "_ "

    return shown_word

def get_guess(guessed_letters):
    while True:
        print()
        print("Guessed so far:", " ".join(guessed_letters))
        guess = input("Enter ONE new letter: ").lower().strip()

        print("You typed:", guess)

        if len(guess) != 1:
            print("Please enter only one letter, for example: e")
        elif not guess.isalpha():
            print("Please enter a letter from A to Z.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess

def check_win(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def play_game():
    secret_word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")
    print("Guess the word before the man is fully drawn.")

    while True:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word:", display_word(secret_word, guessed_letters))
        print("Guessed letters:", " ".join(guessed_letters))
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

        print("-" * 20)

def main():
    while True:
        play_game()

        again = input("Play again? y/n: ").lower().strip()

        if again != "y":
            print("Thanks for playing!")
            break
main()


