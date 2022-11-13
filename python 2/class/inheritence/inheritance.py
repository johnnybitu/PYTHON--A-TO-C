class father:
    money = 1000
    def show(self):
        print("parent class instance method")
    @classmethod
    def showmoney(cls):
        print("parent class class method", cls.money)


class son(father):
    def disp(self):
        print("child class instane method")


s = son()

s.disp()
s.show()
s.showmoney()




### single inheritance 



class student:


    school = str(input("write your school name"))


    def __init__(self):


        self.first= str(input("your first name"))


        self.roll = str(input("write your roll numer"))


    def sub(self):

        
        self.sub= str(input("choose your subject"))

        return(self.sub)


    @classmethod

    def school_name (cls):


        print(cls.school)



class candidate(student):


    def village1(self):

        self.village= str(input("your village name "))
        return self.village
    

arun = candidate()

print(f'my name is ---{arun.first}--my roll number {arun.roll}--my village name---{arun.village1()}----my school name ---{arun.school} and my subject----{arun.sub()}')