print("************************")
print("* Welcome to My Games! *")
print("************************")

game_flag = False

print("(1) The Hangman Game")
print("(2) The Guessing Game")
game = int(input("Choose your game: "))

while(game_flag != True):
    if(game == 1):
        print("The Hangman Game")
        game_flag = True
    elif(game == 2):
        print("The Guessing Game")
        game_flag = True
    else:
        print("(1) The Hangman Game")
        print("(2) The Guessing Game")
        game = int(input("Choose your game: "))