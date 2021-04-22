print("*********************************")
print("* Welcome to the Guessing Game! *")
print("*********************************")

secret_number = 43
total_attempts = 3

for attempt in range(1, total_attempts+1):
    print("Round {} of {}".format(round, total_attempts))
    guess = input("Type an integer number of your choice: ")

    print("You typed ", guess)
    int_guess = int(guess)

    if secret_number == int_guess:
        print("You chose the right number! Congrats!")
    elif int_guess > secret_number:
        print("You chose the wrong number! You guessed a greater number!")
    else:
        print("You chose the wrong number! You guessed a smaller number!")


print("The End")