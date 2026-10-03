'''
Student Subjects
student1 = {"Math", "Python", "DBMS", "OS"}
student2 = {"Python", "OS", "Java", "CN"}

Find:

Dono students ke common subjects
Sirf student1 ke subjects
Sirf student2 ke subjects
Saare unique subjects  '''

student1 = {"Math", "Python", "DBMS", "OS"}
student2 = {"Python", "OS", "Java", "CN"}

result = student1.intersection(student2)
print("Common subjects:", result)

result = student1.difference(student2)
print("Student1's unique subjects:", result)

result = student2.difference(student1)
print("Student2's unique subjects:", result)

result = student1.union(student2)
print("All unique subjects:", result)