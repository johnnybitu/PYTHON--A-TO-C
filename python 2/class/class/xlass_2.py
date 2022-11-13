
class name:
    def __init__(self, name, age , salary):
        self.name = name
        self.age = age
        self.salary = salary
    def company(self,name1):
        company_name =name1
        return company_name

anum = name('tony', 23,  34000)
aa=anum.company('fractral')
print(aa)

print(f'candidate name------- {anum.name}, this is age {anum.age}, -------{anum.salary}--------company name {aa}')