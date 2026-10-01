'''Ek rectangle ki length aur breadth input lo aur calculate karo:

Area
Perimeter'''

length = float (input("Enter the length of the rectangle: "))
breadth = float (input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of the rectangle is:", area)
print("Perimeter of the rectangle is:", perimeter)