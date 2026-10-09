x = 10  #global varibles
def show():
    x=14 # local varibles
    print(x)
show()
print(x)    

x = 10  
def show1():
    global x #global keyword convert local to global
    x = 58
    print(x)
show1()
print(x)    
