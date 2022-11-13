import re


class father:
    def show(self):
        self.id = int(input('this is id'))
        return self.id


class son(father):
    def show1(self):
        self.name = str(input('this is name'))
        return self.name

class grandson(son):
    def show2(self):
        self.last_name = str(input('this is my last name'))
        return self.last_name


arun = grandson()

print(arun.show())
print(arun.show1())
print(arun.show2())
print(arun.name)

# with constructor

class school:
    def __init__(self):
        self.name = 'johnny'
    def non(self):
        return self.name

class student(school):
    def __init__(self):
        super().__init__()
        self.last = 'many'
    def sss (self):
        return self.last

class ideee(student):
    def __init__(self):
        super().__init__()
        self.idea = 4464
    def sub(self):
        return self.idea

a = ideee()
print(a.name)
print(a.non())
print(a.sss())
print(a.idea)
print(a.sub())

