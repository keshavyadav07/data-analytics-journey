'''morning_batch = {"Aman", "Rahul", "Keshav", "Rohit"}
evening_batch = {"Keshav", "Rohit", "Vikas", "Ankit"}

Find:

Dono batches mein common students
Sirf morning batch ke students
Sirf evening batch ke students
Total unique students'''

morning_batch = {"Aman", "Rahul", "Keshav", "Rohit"}
evening_batch = {"Keshav", "Rohit", "Vikas", "Ankit"}
result = morning_batch.intersection(evening_batch)
print("Common students:", result)

result = morning_batch.difference(evening_batch)
print("Morning batch unique students:", result)

result = evening_batch.difference(morning_batch)
print("Evening batch unique students:", result)

result = morning_batch.union(evening_batch)
print("Total unique students:", result)