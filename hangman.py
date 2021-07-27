def play():
    print("********************************")
    print("* Welcome to the Hangman Game! *")
    print("********************************")

    secret_word = "banana"
    guessed_letters = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    guessed = False

    print(guessed_letters)

    #Loop for the game
    while not hanged and not guessed:

        guess = input("Which letter?")
        guess = guess.strip()

        index = 0
        for letter in secret_word:
            if guess.upper() == letter.upper():
                guessed_letters[index] = guess
            index = index + 1

        print(guessed_letters)

    print("The End!")

if __name__ == "__main__":
    play()