
class tony:
    def __init__(self, x,y,z):
        self.x =x
        self.y = y
        self.z= z

gg= tony('tonn', 23,7899) 
print(gg.x)
print(gg.y)
print(gg.z)





class ohnny:
    def __init__(self, x,y,z):
        self.name = x
        self.age = y
        self.year  = z
    def agee(self, current):
        return current - self.year

xx = ohnny('tonyu',23,1996)

print(xx.age)
print(xx.agee(2009))




class mobile :
    def __init__(self):
        self.model = 'real me x'

    def show(self):
        print('model', self.model)


real = mobile()

real.show()
print(real.model)



class name1 :
    def __init__(self, p):
        self.name = p
    def age (self, a):
        age = a
        print(self.name, age)

xx = name1('tony')
print(xx.name)
print(xx.age(300))

