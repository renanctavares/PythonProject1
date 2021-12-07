import random

def play():

    print_title()

    secret_word = load_secret_word()

    guessed_letters = initialize_guessed_words(secret_word)
    print(guessed_letters)

    hanged = False
    guessed = False
    failures = 0

    #Loop for the game
    while not hanged and not guessed:

        guess = ask_guess()

        if guess in secret_word:
            mark_right_guesses(guess, guessed_letters, secret_word)
        else:
            failures += 1

        hanged = failures == 6
        guessed = "_" not in guessed_letters
        print(guessed_letters)

    if guessed:
        print("Congratulations! You won!")
    else:
        print("Oh I'm sorry! You lost!")

def print_title():
    print("********************************")
    print("* Welcome to the Hangman Game! *")
    print("********************************")

def load_secret_word():
    words = []

    with open("/Users/renancostatavares/Documents/GitKraken/PythonProject1/words.txt", "r") as file:
        for line in file:
            words.append(line.strip())

    word_id = random.randrange(0, len(words))

    secret_word = words[word_id].upper()
    return secret_word

def initialize_guessed_words(secret_word):
    return ["_" for letter in secret_word]

def ask_guess():
    guess = input("Which letter?")
    guess = guess.strip().upper()
    return guess

def mark_right_guesses(guess, guessed_letters, secret_word):
    index = 0
    for letter in secret_word:
        if guess == letter:
            guessed_letters[index] = guess
        index += 1

if __name__ == "__main__":
    play()