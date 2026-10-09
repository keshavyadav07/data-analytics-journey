#update funtion
x = 10
def update():
    global x
    x = 50

update()
print(x)

#change funtion

x = 100

def change():
    x = 200
    print("Inside:", x)

change()
print("Outside:", x)