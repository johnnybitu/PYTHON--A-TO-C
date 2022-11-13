from bank_details.bank_form import addressing,official,information


from time import ctime



class passbook(addressing,official,information):
    def __init__(self):
        super().__init__()
        ad = str(self.adhar)
        pan = str(self.pan)
        pin = str(self.pincode)
        self.accountnumber = '6605'+ad[:5] +pan[0:3] +pin[0 : 3]
        self.ifsc = 'sbi'+self.district[0:2] +pin[0 : 2] +'458'
    def passboo(self):
        return f'ACCOUNTNUMBER {self.accountnumber}\n IFSC {self.ifsc}\n  \n'

a = input('(your first name): ')
b   = (a.upper())


directory ="E:\complete datascience\python\PROJECTS\project - BANK PASSBOOK AND TRANSACTION GENERATOR\passbook_transaction//" 
filepath = directory+b




with open(filepath, mode='a+') as f:

    
    details = passbook()
    a = ctime()
    


    f.write('STATE BANK OF INDIA \n \n')
    f.writelines(f'{details.show1()} \n ')
    f.writelines(f'OFFICAL DETAILS\n{details.show()}\n ')
    f.writelines(f'ADDRESS:\n{details.show2()}\n')
    f.write(f'ACCOUNT NUMBER{details.accountnumber}\nIFSC :{details.ifsc}\n ')
    

    f.write(f'DIGITAL GENERATED PASSBOOK {a}\n')
    f.close()
    




