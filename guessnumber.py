from random import seed
from random import randint

thisnumber = randint(1, 100)

guess = int(input("I'm thinking of a number between 1 and 100... "))

while guess != thisnumber:
    if guess < thisnumber:
        print("No...higher!")
    elif guess > thisnumber:
        print("No...lower!")
    guess = int(input("Try again: "))
else: print("Correct!")

print(thisnumber)