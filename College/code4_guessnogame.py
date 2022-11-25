# Guess Number Game
import random  # imports random file function
r = random.randint(1, 20)  # it will generate a random number between 1 to 20.

while (True):  # true condition
    print("Enter the no. : ")
    n = int(input())
    if (n < r):
        print("Wrong Guess, try a greater number")
    elif (n > r):
        print("Wrong Guess, try a smaller number")
    else:
        print("Congrats, you've guessed the number ")
        break
