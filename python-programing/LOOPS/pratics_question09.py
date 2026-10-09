'''GCD / HCF
Do numbers input lo aur loop se HCF find karo.

Input:
24 36

Output:
12'''
a,b = map(int, input("Enter two numbers: ").split())

hcf = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print(hcf)




'''LCM

Input:
12 18

Output:
36'''


a,b = map(int, input("Enter two numbers: ").split())

lcm = max(a, b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print(lcm)