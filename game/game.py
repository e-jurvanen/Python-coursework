import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                pass
            else:
                break
        except ValueError:
            pass


    ran_no = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > ran_no:
                print("Too large!")
            elif guess < ran_no:
                print("Too small!")
            elif guess == ran_no:
                sys.exit("Just right!")
        except ValueError:
            pass

main()
