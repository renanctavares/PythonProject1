def play():
    print("********************************")
    print("* Welcome to the Hangman Game! *")
    print("********************************")

    secret_word = "banana"

    hanged = False
    guessed = False

    #Loop for the game
    while not hanged and not guessed:

        guess = input("Which letter?")
        guess = guess.strip()

        index = 0
        for letter in secret_word:
            if guess.upper() == letter.upper():
                print("Found letter {} in position {}.".format(guess, index))
            index = index + 1

    print("The End!")

if __name__ == "__main__":
    play()