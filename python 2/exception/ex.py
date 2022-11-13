a = int(input('this is a '))
b = int(input('this is b '))
try:
    d =a/b
    print(d)
except ZeroDivisionError:
    print('ZeroDivisionError')



print('rest of the codde')

c = int(input('this is c '))
g = int(input('this is g '))

try:
    h = c/g
    print(h)
except ZeroDivisionError as obj:
    print(obj)
else:
    print("no exccption raid")
finally:
    print('i am the last one')