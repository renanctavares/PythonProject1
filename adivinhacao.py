print("*********************************")
print("* Welcome to the Guessing Game! *")
print("*********************************")

secret_number = 43

guess = input("Type an integer number of your choice: ")

print("You typed ", guess)

if secret_number == int(guess):
    print("You chose the right number! Congrats!")
else:
    print("You chose the wrong number! Try again!")

print("The End")