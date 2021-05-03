import random

print("*********************************")
print("* Welcome to the Guessing Game! *")
print("*********************************")

secret_number = random.randrange(1, 101)
total_attempts = 3

for attempt in range(1, total_attempts+1):
    print("Round {} of {}".format(attempt, total_attempts))
    guess = input("Type an integer number between 1 and 100: ")

    print("You typed ", guess)
    int_guess = int(guess)
    if int_guess < 1 or int_guess > 100:
        print("You must type a number between 1 and 100")
        continue

    if secret_number == int_guess:
        print("You chose the right number! Congrats!")
        break
    elif int_guess > secret_number:
        print("You chose the wrong number! You guessed a greater number!")
    else:
        print("You chose the wrong number! You guessed a smaller number!")


print("The End")