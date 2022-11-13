aa = lambda x,y : print(x+y)
print(aa(5,6))

add = lambda x,y :(x+y, x-y)
a,s = add(8,9)
print(a)
print(s)


xxx= lambda xx=10:(lambda y :xx+y)
a = xxx()
print(a(20))