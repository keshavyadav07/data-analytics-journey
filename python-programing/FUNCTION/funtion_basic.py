def greet():
    print("hey sir,\nhow are you\nthankyou so mush ")
greet()

def greet(name,city):
    print("hellow",name ,"location",city)
greet("keshav","indore")   


def greet(name ="user",city = "indore"):
    print("hellow",name ,"location",city)
greet()    
greet("keshav","indore")   


def add(a,b):
    print(a+b)
add(8,12)    
c = add(10,12)
print(c)


def add(a,b):
    return a+b
k = add(8,12)    
c = add(10,12)
print(c,k)


# *args

def total(*args):
    print(args)
total(1,2,3,4,5,6,7,8,9) 

# **kwargs

def user_details(**kwargs):
    print(kwargs)
user_details(name ="keshav",age="19",city="indore",degree="b.tech")    
