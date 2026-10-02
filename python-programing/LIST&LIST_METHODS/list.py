RSS = ["KESHAV", "AJESH", "AYUSH", "DIPESH","VASU"]
print(RSS)
print("Length of the list:", len(RSS))
print(RSS[2])  # Accessing the third element (index 2)
print(RSS[-1])  # Accessing the last element (index -1)
print(type(RSS))  # Checking the type of the list   
print(RSS[1:4])  # Slicing the list from index 1 to 3

'''list in python is mutable
mtlb list ko badal sakte h biche m'''
RSS[1] = "yadav"
print(RSS)  # Output: ['KESHAV', 'yadav', 'AYUSH', 'DIPESH', 'VASU']