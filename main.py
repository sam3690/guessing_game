import random


def guessing_game (num):
    number = random.randint(0,10)

    if num == number:
           print ("Guess the number for 0 to 10: ")
           return print (f"""You guessed the number! it's {num}!""")
    else:
        print("you guessed wrong!")


guessing_game(1)