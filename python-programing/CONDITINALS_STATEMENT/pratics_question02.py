Electricity_unit = int(input("enter your electricity unit: "))

if Electricity_unit <= 100:
    bill = Electricity_unit * 5
    print("your electricity bill is: ", bill)
elif Electricity_unit <= 200:
    bill = Electricity_unit * 7
    print("your electricity bill is: ", bill)
else:
    bill = Electricity_unit * 10
    print("your electricity bill is: ", bill)