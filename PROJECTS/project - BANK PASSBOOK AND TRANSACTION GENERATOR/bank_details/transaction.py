


class open :
    def __init__(self):
        self.open_charge = 5000

class deposite(open):
    def __init__(self):
        super().__init__()
        self.deposite = int(input('INPUT YOUR DEPOSITE MONEY AMOUNT (or you can type 0 if you want to withdrawl) :'))
        self.balance = self.deposite+self.open_charge



class withdrawl(deposite):
    def __init__(self):
        super().__init__()
        self.withdrawl = int(input('INPUT YOUR WITHDRAWL MONEY AMOUNT 0 if you deposited your money:'))
    def total (self):

        if self.balance < self.withdrawl:
            print('insufficiant balance ')
        else:
            total_bal  = self.balance  - self.withdrawl
            return f'opening balance {self.open_charge}  \n DEPOSITE :{self.deposite}\n WITHDrawl :{self.withdrawl}\n  BALANCE:{total_bal}\n'


