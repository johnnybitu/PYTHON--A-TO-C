class mobile:
    def __init__(self):
        self.model = str(input('this will model name--------'))       # this is instance variable 
        self.prince = int(input('this is the price-------'))           # this is also instance 
    def show(self):
        print(f'this is the model name --------{self.model} and it\'s price ----------{self.prince}')     # accessing instance variable 

realme = mobile()
realme.show()
print('this is model name ----------',realme.model)                        # accessing outside
print('this is the price ----------',realme.prince)


redmi= mobile()
redmi.show()
print('this is model name ----------',redmi.model)
print('this is model name ----------',redmi.prince)

nokia = mobile()
nokia.show()
print('this is model name ----------',nokia.model)
print('this is model name ----------',nokia.prince)



class studen:
    # instance method
    def show(self):
        print('my name is ')

john = studen()
john.show()

class stand:
    def __init__(self):
        self.up = 'stdan up'
    def sit(self, jo):
        self.sitdown= jo
        print(self.sitdown)
    
ssss = stand()
ssss.sit(2000)

