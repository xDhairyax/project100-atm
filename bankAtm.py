import random

class atm():
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number

    def viewCash(self):
        number=random.randint(10000,100000)
        print("this much balance is there:"+str(number))

    def cashwithdrawl(self,amount):
        new_amount=amount-10000
        print("Your Remaining Balance is:"+str(new_amount))


def main():
    cardnumber=input("Enter Your Card Number:")
    pinnumber=input("Enter Your Pin Number:")

    user=atm(cardnumber,pinnumber)

    print("What do u want to see")
    print("1)Want to View Your Money or 2)Withdraw Money")
    view=int(input("Where do u want to go 1 or 2:"))

    if view==1:
        user.viewCash()
    
    elif view==2:
        user.cashwithdrawl(20000)

    else:
        print("invalid option,print '1' or '2' ")

main()


    

