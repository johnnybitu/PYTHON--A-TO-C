import pickle 
class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def disp(self):
        print(self.name , self.roll)


with open('student.dat', mode='wb') as f:
    stu = student('johny', 101)
    pickle.dump(stu,f)
    print("pickle success full")



with open('student.dat', mode='rb') as f:
    obj = pickle.load(f)
    print('unpickling done')
    obj.disp()