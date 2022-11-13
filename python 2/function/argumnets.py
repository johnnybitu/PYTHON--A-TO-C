# positional argumnet
def pw(a ,b):
    x = a**b
    print(x)
pw(5,2)

# number of formal argument == number of actual arguments

# keyword argumnet
def name (x ,y):
    print(x,y)
name(x= 'johnny', y = 62)

# number of FA should be equal to number of actual argumnet

 # default argument

def ssw(nn, aa= 62):
    print(nn, aa)
ssw(nn= 45)

def ssw(nn1, baa= 62):
    print(nn1, baa)
ssw(nn1= 45,baa=89 )


# variable length argumnet

def aim (*len):
    z= len[0]+len[1]
    print(z)
aim(5,6)

def aim (x,*len):
    p= x+len[0]+len[1]
    print(p)
ab = aim(5,6,7,8,10)
print(ab)
#  keyword value argument

def add(**m):
    z= m['a']+m['b']
    print(z)
add(a=2, b= 4)

