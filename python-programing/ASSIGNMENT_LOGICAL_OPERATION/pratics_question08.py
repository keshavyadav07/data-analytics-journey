age = int(input("Enter your age: "))
has_id = input("Do you have ID? (True/False): ")

has_id = has_id == "True"

result = age >= 18 and has_id

print(result)