x = 1

def fun():
    global x
    x = x + 2
    print(x)

fun()
fun()
fun()

print(x)
# no change but same concept
def counter():
    count = 0
    count = count + 1
    print(count)

counter()
counter()
counter()

# doo global varibles
x = 10

def test():
    global x
    x = 20
    x = 30
    print(x)

test()
print(x)

total = 100

def add():
    global total
    total = total + 50

add()
print(total)