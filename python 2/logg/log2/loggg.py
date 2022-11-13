import logging

logging.basicConfig(level=logging.ERROR ,
                    
                    filename='E:\complete datascience\python\python 2\logg\log2//new.log',
                    filemode='a',
                    format='%(message)s - %(levelname)s - %(filename)s - %(message)s - %(levelname)s - %(asctime)s')
 
try:
    class metr:
        logging.info('this is ok')
        def __init__(self):
            self.bank = int(input('a'))
            self.money = int(input('a'))
        def show(self):
            
            return self.bank, self.money
    
    a = metr()

except:
    logging.error('a error has happend')
