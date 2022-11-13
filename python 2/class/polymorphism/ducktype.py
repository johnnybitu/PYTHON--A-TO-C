class duck :
    def walk(self):
        print("tapak tapak")
class cat:
    def talk(self):
        print("mew mew")

class horse:
    def walk (self):
        print("tabdak")

def myfunction(m):
    m.talk()

def myfunc(g):
    g.walk()

d = duck()
a = horse()
b = cat()

du = myfunc(d)
ho = myfunc(a)
ca = myfunction(b)



