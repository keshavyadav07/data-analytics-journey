age = int(input("enter your age: "))
if age>=0 or age<=10:
    print("you are a child")
elif age>=11 or age<=20:
    print("you are a teenager")
elif age>=21 or age<=60:   
    print("you are an adult")
elif age>60:
    print("you are a senior citizen")