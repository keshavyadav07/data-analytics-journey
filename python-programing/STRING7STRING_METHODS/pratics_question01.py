'''User se ek string input lo. Print karo:

Total characters
First character
Last character
Middle character (agar length odd hai)'''

string = input("Enter a string: ")
length = len(string)
print(f"Total characters: {length}")
print(f"First character: {string[0]}")
print(f"Last character: {string[-1]}")
if length % 2 == 1:
    middle_index = length // 2
    print(f"Middle character: {string[middle_index]}")
else:
    print("Middle character: Not applicable (even length)")