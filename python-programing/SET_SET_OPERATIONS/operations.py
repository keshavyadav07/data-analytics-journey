A = {1,5,4,2,3,8,7}
B ={1,2,3,4,5,6,7}

# union opration

result = A.union(B)
print(result)

# intersection operation

result = A.intersection(B) 
print(result)

# difference operation
result = A.difference(B)  # result = A - B
print(result)


# symmetric operation
result = A.symmetric_difference(B)  # result = A ^ B
print(result)