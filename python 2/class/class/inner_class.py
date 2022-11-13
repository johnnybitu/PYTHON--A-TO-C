class school:
    def __init__(self):
        self.name= str(input('student name -----'))
        self.sub= self.sub_name()
    def show(self):
        return("name ", self.name)
    class sub_name:
        def __init__(self):
            self.name  = 'rahul singh'
            self.capacity = 8966
            self.lenn = self.length()
        def show1(self):
            print(self.name, self.capacity)
        class length:
            def __init__(self):
                self.leng = 'this is the length'
            def show3(self):
                print(self.leng)

harvard = school()

print(harvard.name)
print(harvard.show())
print(harvard.sub.capacity)
print(harvard.sub.lenn.leng)
print(harvard.sub.lenn.show3())
