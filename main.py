import random

def main():
    # create 3 levels easy,med,hard
    level = input("Enter your level: ")
    if level == "easy":
        number = random.randint(0, 10)
        upper_limit = 10
    elif level == "medium":
        number = random.randint(0, 50)
        upper_limit = 50
    elif level == "hard":
        number = random.randint(0, 100)
        upper_limit = 100

    guess = int(input(f"Guess a number between 0 and {upper_limit}: "))

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

