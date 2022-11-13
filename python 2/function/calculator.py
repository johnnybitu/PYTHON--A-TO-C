def calculator():
    x = int(input('this is x'))
    y = int(input('this is y'))
    c = input('this is symbol')

    if c =='*':
        print(x*y)
    elif c == '+':
        print(x+y)
    elif c == '-':
       print(x-y)
    elif c == '/':
        print(x/y)
calculator()

# with argument


def calculator(a,b,d):
    
    if d =='*':
        print(a*b)
    elif d == '+':
        print(a+b)
    elif d == '-':
       print(x-y)
    elif d == '/':
        print(a/b)
calculator(a =int(input('this is a')),
           b = int(input('this is b')),
           d = input('this is symbol') )
