import random

def play():
    print("********************************")
    print("* Welcome to the Hangman Game! *")
    print("********************************")

    words = []

    with open("/Users/renancostatavares/Documents/GitKraken/PythonProject1/words.txt", "r") as file:
        for line in file:
            words.append(line.strip())

    word_id = random.randrange(0, len(words))

    secret_word = words[word_id].upper()
    guessed_letters = ["_" for letter in secret_word]

    hanged = False
    guessed = False
    failures = 0

    print(guessed_letters)

    #Loop for the game
    while not hanged and not guessed:

        guess = input("Which letter?")
        guess = guess.strip().upper()

        if guess in secret_word:
            index = 0
            for letter in secret_word:
                if guess == letter:
                    guessed_letters[index] = guess
                index += 1
        else:
            failures += 1

        hanged = failures == 6
        guessed = "_" not in guessed_letters
        print(guessed_letters)

    if guessed:
        print("Congratulations! You won!")
    else:
        print("Oh I'm sorry! You lost!")
    print("The End!")

if __name__ == "__main__":
    play()