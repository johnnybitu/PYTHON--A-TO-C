from abc import ABC , abstractclassmethod

class father (ABC):
    @abstractclassmethod
    def dis(self):
        pass
    def show(self):
        print("concreate method")

class child(father):
    def dis(self):
        print("child classs")
        print("abstract method")


c = child()
c.dis()
c.show()
