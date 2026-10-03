'''keshav = {"Python", "SQL", "Excel", "Power BI"}
rahul = {"Python", "Java", "SQL", "C++"}

Find:

Common skills
Keshav ke unique skills
Rahul ke unique skills
Dono ki total unique skills'''

keshav = {"Python", "SQL", "Excel", "Power BI"}
rahul = {"Python", "Java", "SQL", "C++"}

result = keshav.intersection(rahul)
print("Common skills:", result)

result = keshav.difference(rahul)
print("Keshav's unique skills:", result)

result = rahul.difference(keshav)
print("Rahul's unique skills:", result)

result = keshav.union(rahul)
print("All unique skills:", result)