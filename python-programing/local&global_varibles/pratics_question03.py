#  same varibles name
print("same varibles name")
name = "Keshav"

def student():
    name = "Rahul"
    print(name)

student()
print(name)

#global varibles with tow funtion
print("global varibles with tow funtion")

count = 0

def increase():
    global count
    count = count + 1

def display():
    print(count)

increase()
increase()
display()

