

import os 


a = input('YOUR PASSBOOK NAME(your first name) : ')
b   = (a.upper())
directory ="E:\complete datascience\python\PROJECTS\project - BANK PASSBOOK AND TRANSACTION GENERATOR\passbook_transaction//" 
filepath = directory+b


import os 

exist = os.path.exists(filepath)

if exist == True:
    from time import ctime
    from bank_details.transaction import withdrawl
    with open(filepath, mode='a+') as f:
        bb = ctime()
        a = withdrawl()
        f.write(f'\n YOUR TRANSACTION \n{a.total()} {bb} \n')
        f.close()
else:
    print('first open your bank account')
     



