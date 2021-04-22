print("*********************************")
print("* Welcome to the Guessing Game! *")
print("*********************************")

secret_number = 43
total_attempts = 3
round = 1

while round <= total_attempts:
    print("Round", round, "of", total_attempts)
    guess = input("Type an integer number of your choice: ")

    print("You typed ", guess)
    int_guess = int(guess)

    if secret_number == int_guess:
        print("You chose the right number! Congrats!")
    elif int_guess > secret_number:
        print("You chose the wrong number! You guessed a greater number!")
    else:
        print("You chose the wrong number! You guessed a smaller number!")

    round = round + 1

print("The End")