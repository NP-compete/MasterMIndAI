#Mastermind Board Game
import sys
import numpy as np
from collections import Counter
from itertools import product
import ai_module.ai as AI
import random


ai = False
game = True

print (" --- MASTERMIND --- \n")
print ("Guess the secret color code in as few tries as possible.\n")

answer = input("Choose 1 to play yourself or 2 to watch the AI play: ")

if answer == '1':
    print("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W), purple(P)")
    print("An example guess could be: GGBB")
    print("An 'X' in the reply means a correct colour in a correct place.")
    print("An 'O' in the reply means a correct colour in the wrong place.\n")
elif answer == '2':
    ai = True
    game = False
else:
    print("Wrong input.")
    sys.exit(-1)




colors = 'RBYGWP'  # Allowed colors

#Generating random secret code
code = ""
for i in range(0,4):
    code += random.choice(colors)

X = np.array([])
attempts = 0

while game:
    print("\n" + "*#" * 43)
    print("\nPast tries:")
    print(X)
    print("Possible colors: {}".format(colors))
    if ai:
        pass
    else:
        guess = input("Attempt {}: ".format(attempts+1)).upper()

        if len(guess) != len(code):
            print("Invalid Input")
            continue

        out = False
        for i in range(len(guess)):
            if guess[i] not in colors:
                print("{} Is invalid input, not a possible color".format(guess[i]))
                out = True
        if (out):
            continue
    

        if guess == code:
            print("Congratulations you did it in {} attempts".format(attempts+1))
            print(X)
            break

        if attempts > 10:
            print("Sorry you didnt make it, you only have 10 attempts.")
            print("The correct color code was {}.".format(code))
            break
        else:
            left, right = AI.evaluate(guess, code)
            reply = []
            reply.append(["X" for _ in range(left)])
            reply.append(["O" for _ in range(right)])
            print(reply)


        guess = np.array(guess)
        guess = np.append(guess, left)
        guess = np.append(guess, right)

        X = np.append(X, np.array(guess))
        X = np.reshape(X,(attempts+1, 3))

        attempts += 1

if ai == True:
    #Defining all possbile states
    All_Codes = [''.join(i) for i in product(colors, repeat=4)]
    print("Input a code for the computer to solve, eg. BWWG.")
    print("\n")
    print("Possible colors {}".format(colors))
    print("\n")
    code = input("Input code here: ").upper()
    #Here we load in the AI.
    AI.MINIMAX(code,All_Codes)


#The Output of the game will be vector X with shape (attempts,6)
#Column 4 is the amount of guesses you got correctly
#column 5 is the amount of colors you got correctly but placed wrong
