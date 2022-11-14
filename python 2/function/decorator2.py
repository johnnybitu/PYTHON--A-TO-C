def surname(sur):
    def inner():
        a = sur()
        b = a + 'bit'
        return b
    return inner
def first_name():
    return 'johnny'

name = surname(first_name)
print(name())


def name(n):
    def inner():
        a = n()
        c = int(input('multiply'))
        b = a * c
        return b
    return inner

@name

def mobile():
    a = int(input('your mobile number:'))
    return a

print(mobile())


def decor1(num):
    def inner():
        b = num()
        multi= b*5
        return multi
    return inner
def decor(num):
    def inner():
        a = num()
        multi= a*5
        return multi
    return inner

def num():
    return 10

num = decor(decor1(num))
print(num())
