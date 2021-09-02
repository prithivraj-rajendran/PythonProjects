# This code will tell an atm machine that how many notes at each amount to be given to user.
if __name__=="__main__":
    notes = [2000, 1000, 500, 100, 50, 20, 10]
    amount=int(input("Enter the amount to withdraw "))
    if amount%10==0:
        for note in notes:
            if amount>=note and amount>0:
                count=0
                count=amount//note
                amount=amount-(count*note)
                print("{} * {} = {}".format(note,count,note*count))
            else:
                continue
    else:
        print("Please enter an amount in multiples of 10")