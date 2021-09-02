import random

# This method will return score value
def score(com_guess, user_guess):
    a = {
        'stone': {
            'paper': 1,
            'scissor': -1,
            'stone': 0
        },
        'scissor': {
            'paper': -1,
            'stone': 1,
            'scissor': 0
        },
        'paper': {
            'stone': -1,
            'scissor': 1,
            'paper': 0
        }
    }
    return a.get(com_guess).get(user_guess)

if __name__=="__main__":
    print("Let's start the game....")
    params = ['stone', 'paper', 'scissor']
    sc = 0
    for x in range(5):
        com_guess = random.choice(params)
        print("{} of {} chance".format(x+1,5))
        user_guess = input("Guess ")
        print("Computer guessed {}".format(com_guess))
        temp_sc= score(com_guess.casefold(), user_guess.casefold())
        sc=sc+temp_sc if temp_sc is not None else sc
    if sc > 0:
        print("Hurrah!!! You Won")
        print("Final Score {}".format(sc))
    elif sc==0:
        print("Ouch!! match went draw")
    else:
        print("Oops!!! Better Luck Next Time")
