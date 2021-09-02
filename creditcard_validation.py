# This fn will check for consecutive digits
def con_num(a):
    count=0
    b=[]
    for x in range(len(a)):
        if a[x].isdigit():
            b.append(a[x])
    for x in range(len(b)-1):
        if b[x]==b[x+1]:
            count+=1
            if count>=3:
             return False
        else:
            count=0
    else:
        return True
if __name__=="__main__":
    num=int(input("Enter the number of credit cards to validate "))
    cards=list()
    for x in range(num):
        card=input("Card {} ".format(x+1))
        cards.append(card)
    for x in cards:
        i=con_num(x)
        if i==True:
            if x.startswith('4') or x.startswith('5') or x.startswith('6'):
                if len(x)==19:
                    if(x[4]==x[9]==x[14]=='-'):
                        print(x," - Valid")
                    else:
                        print(x," - Invalid")
                        continue
                elif len(x)==16:
                    print(x," - Valid")
                else:
                    print(x," - Invalid")
                    continue
            else:
                print(x," - Invalid")
                continue
        else:
            print(x," - Invalid")