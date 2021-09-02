import random

# This method will return a hint for an user.
def hint(number,temp_sc):
    if i>number:
        print("Guess above {} " .format(number))
        temp_sc-=1
        guess_crct(temp_sc)
    else:
        print("Guess below {} " .format(number))
        temp_sc-=1
        guess_crct(temp_sc)

# This method will validate user guess
def guess_crct(sc):
    num=int(input("Guess the number "))
    if num not in q:
        q.append(num)
    else:
        print("Already entered")
        guess_crct(sc)
    if i==num or sc<=0:
        print("Wow!!! What a guess") if sc>=1 else print("Better Luck next time")
        print("you scored {}" .format(sc))
    else:
        h=str(input("Need hint(Yes/No) "))
        hint(num,sc) if h.casefold()=='yes' else print("You Failed in the Game")

if __name__=='__main__':
    i=random.randint(1,100)
    q=[]
    score=10
    guess_crct(score)
