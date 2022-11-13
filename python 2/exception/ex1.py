li = [1,2,3,4,5,6,7,8,9]

try:
    for i in li:
        print(i)
        
except:
    print('except raised exception')
    for i in li:
        print(i*'exception')
else:
    print('no exception raised')
    for i in li:
        print(i*'else')
finally:
    print('finally')
    for i in li:
        print(i*'finally')