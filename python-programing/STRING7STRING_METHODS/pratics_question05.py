string = input("Enter a string: ")
character = input("Enter a character: ")

count = string.count(character)

print("Character occurs", count, "times")


#ek aur exmple
text = "I love Python programming"

words = text.split()

print("Words:", len(words))
print("Characters:", len(text))
print("First Word:", words[0])
print("Last Word:", words[-1])