import random

def play():
    print("*********************************")
    print("* Welcome to the Guessing Game! *")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    points = 1000

    print("(1) Easy")
    print("(2) Normal")
    print("(3) Hard")
    level = int(input("Choose a level: "))
    flag_level = False

    while flag_level != True:
        if level == 1:
            total_attempts = 20
            flag_level = True
        elif level == 2:
            total_attempts = 10
            flag_level = True
        elif level == 3:
            total_attempts = 5
            flag_level = True
        else:
            print("(1) Easy")
            print("(2) Normal")
            print("(3) Hard")
            level = int(input("Choose a level: "))

    for attempt in range(1, total_attempts+1):
        print("Round {} of {}".format(attempt, total_attempts))
        guess = input("Type an integer number between 1 and 100: ")

        print("You typed ", guess)
        int_guess = int(guess)
        if int_guess < 1 or int_guess > 100:
            print("You must type a number between 1 and 100")
            continue

        points = points - abs(secret_number - int_guess)

        if secret_number == int_guess:
            print("You chose the right number! Congrats!")
            print("You got {} points!".format(points))
            break
        elif int_guess > secret_number:
            print("You chose the wrong number! You guessed a greater number!")
        else:
            print("You chose the wrong number! You guessed a smaller number!")


    print("The End!")

if __name__ == "__main__":
    play()