class balanceException(Exception):
    pass


def checkblance():
    money= int(input('this is money '))
    withdrawl = int(input('with drawl '))

    try:
        balance = money - withdrawl 
        if balance < 2000 :
            raise balanceException('insufficient balance')
        print("this is your balance ",balance)
    except balanceException as mi:
        print(mi)
checkblance()

## or you can do this 

def checkblance():
    money= int(input('this is money '))
    withdrawl = int(input('withdrawl '))

    balance = money - withdrawl 
    if balance < 2000 :
        raise balanceException('insufficient balance')
    print("this is your balance ",balance)
try:
    checkblance()
except balanceException as be:
    print(be)