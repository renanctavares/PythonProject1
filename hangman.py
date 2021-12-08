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
            draw_hangman(failures)

        hanged = failures == 7
        guessed = "_" not in guessed_letters
        print(guessed_letters)

    if guessed:
        print_winning_message()
    else:
        print_lost_message(secret_word)

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

def print_lost_message(secret_word):
    print("Oh my! You've been hanged!")
    print("The secret word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_winning_message():
    print("Congratulations, you won!")
    print("       ___________       ")
    print("      '._==_==_=_.'      ")
    print("      .-\\:      /-.     ")
    print("     | (|:.     |) |     ")
    print("      '-|:.     |-'      ")
    print("        \\::.    /       ")
    print("         '::. .'         ")
    print("           ) (           ")
    print("         _.' '._         ")
    print("        '-------'        ")

def draw_hangman(failures):
    print("  _______     ")
    print(" |/      |    ")

    if(failures == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(failures == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(failures == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(failures == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(failures == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(failures == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (failures == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    play()