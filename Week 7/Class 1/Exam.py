# QUESION 1

import random

number = random.randint(1,100)
numofguesses = 0


while numofguesses < 6:
    print ("Take a Guess. ")
    guess = input()
    guess = int(guess)


    numofguesses = numofguesses + 1

    if guess < number:
        print("Wrong guess, too low! ")
    if guess > number:
        print("Wrong guess, too high! ")
    if guess == number:
        break
if guess == number:
    print("Correct, you win!")
if guess != number:
    print ("Sorry you are wrong, the correct number was  " + str(number))

