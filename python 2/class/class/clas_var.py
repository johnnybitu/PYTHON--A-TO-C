class school_name:
    school = 'HARVARD SCHOOL AND CODE'
    def __init__(self):
        self.name = str(input('this is student name'))
        self.subject = str(input('this is subject'))
    def show(self):
        self.roll = int(input('this is roll number'))
        return self.roll
    @classmethod
    def sc(cls):
        return  cls.school

candidate = school_name()

print( f'school name ---{school_name.sc()}------yes i am ---------{candidate.name} and my subject--------{candidate.subject} and it\'s my roll number -----{candidate.show()}')


print(school_name.school)




