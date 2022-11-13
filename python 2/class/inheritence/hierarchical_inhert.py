
class father:
    def __init__(self):
        self.dam= "danny"
        self.tan = "tanny"
    def show(self):
        return ("this is father method")

class son(father):
    def __init__(self):
        super().__init__()
        self.ooo = "tonyty"
    def sona (self):
        return("this is sona method")

class daughte(father):
    def __init__(self):
        super().__init__()
        self.ok = "ok mythg"
    def daug(self):
        return("this is mom")

# datughter

arun = daughte()
print(f'{arun.dam, arun.tan, arun.show(), arun.ok, arun.daug()}')


# son
sou = son()
print(f'{sou.dam, sou.tan, sou.show(), sou.ooo, sou.sona()}')


# suppose you and your sister are sibling so you and your sis can acccesss the property of father but you can't access the property of sis and same to  your sis too



