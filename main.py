import random

def main():
    number = random.randint(0, 10)
    guess = int(input("Guess a number between 0 and 10: "))

    while guess != number:
        if guess < number:
            print("Too low")
            guess = int(input("Guess a number between 0 and 10: "))
        elif guess > number:
            print("Too high")
            guess = int(input("Guess a number between 0 and 10: "))

    else: print("You guessed right!")



if __name__ == '__main__':
    main()

