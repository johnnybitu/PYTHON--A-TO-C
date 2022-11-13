from opcode import hasconst


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
    if hasattr(m, 'talk'):

        m.talk()

def myfunc(g):
    if hasattr (g,'walk'):
         g.walk()

d = duck()
a = horse()
b = cat()

du = myfunc(d)
ho = myfunc(a)
ca = myfunction(b)



