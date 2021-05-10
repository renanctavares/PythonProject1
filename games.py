import guessing
import hangman

def choose_game():
    print("************************")
    print("* Welcome to My Games! *")
    print("************************")

    game_flag = False

    print("(1) The Hangman Game")
    print("(2) The Guessing Game")
    game = int(input("Choose your game: "))

    while(game_flag != True):
        if(game == 1):
            hangman.play()
            game_flag = True
        elif(game == 2):
            guessing.play()
            game_flag = True
        else:
            print("(1) The Hangman Game")
            print("(2) The Guessing Game")
            game = int(input("Choose your game: "))

if __name__ == "__main__":
    choose_game()