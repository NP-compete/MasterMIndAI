from collections import Counter
from itertools import product

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def evaluate(guess,code):
    All_matches = sum((Counter(code) & Counter(guess)).values())
    left = sum(i == j for i, j in zip(guess, code))
    right = All_matches - left
    return left, right

def MAX_VALUE(guess,States):
    evaluation_list = []
    for i in range(len(States)):
        evaluation_list.append(evaluate(guess,States[i]))
    evaluation_list_count = Counter(evaluation_list).values()
    MAX_count = max(evaluation_list_count)
    return MAX_count

def MINIMAX(code,All_Codes):
    best_guess = "YYRR"
    minimum = len(All_Codes)
    States = All_Codes
    guess_count = 1
    while True:
        eval_guess = evaluate(best_guess,code)
        print("\n")
        print(bcolors.HEADER + "AI's guess nr. {}: Guess {}. Evaluate: {}".format(guess_count, best_guess,eval_guess) + bcolors.ENDC)
        if best_guess == code:
            print("\n")
            print("The AI have guessed the secret code {} in {} tries".format(code,guess_count))
            break
        States = [i for i in States if evaluate(best_guess, i) == eval_guess]
        print
        print("{} possible states: {}".format(len(States),States))

        if len(States) == 1:
            best_guess = States[0]
        else:
            for i in range(len(States)):
                MAX_count = MAX_VALUE(States[i],States)
                if MAX_count < minimum:
                    minimum = MAX_count
                    best_guess = States[i]
                if States[i] == code:
                    break

        guess_count += 1
