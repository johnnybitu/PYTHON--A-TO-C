class father:
    def __init__(self):
        super().__init__()
        self.na = "no"
        self.yes = "yes"
        self.tim = "tim"
    def show(self):
        self.tim = "tim"
        return self.tim

class child1(father):
    def __init__(self):
        super().__init__()
        self.non = "non"
        self.yess = "yes"
    def show1(self):
        self.tim1 = "timm1"
        return self.tim1

class child2(father):
    def __init__(self):
        super().__init__()
        self.non1 = "non1"
        self.ye = "ye"
    def show2(self):
        self.tim2 = "tim2"
        return self.tim2

class grand(child1, child2):
    def __init__(self):
        super().__init__()
        pass



johnny = grand()
print(johnny.show2())
print(johnny.non1)
print(johnny.tim2)
print(johnny.show1(),johnny.tim1)