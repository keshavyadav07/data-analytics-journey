'''Prime Numbers in Range

print_primes(start, end) function banao jo given range ke saare prime numbers print kare.'''

def print_primes(start, end):
    for n in range(start, end + 1):

        if n < 2:
            continue

        is_prime = True

        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            print(n)


start = int(input("Enter start: "))
end = int(input("Enter end: "))

print_primes(start, end)


'''Fibonacci Function

fibonacci(n) function banao jo first n Fibonacci numbers print kare'''

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")

        c = a + b
        a = b
        b = c


n = int(input("Enter n: "))

fibonacci(n)

'''Second Largest 🔥

second_largest(numbers) function banao jo list ka second largest element return kare.'''

def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second


numbers = list(map(int, input("\nEnter numbers: ").split()))

print("Second Largest:", second_largest(numbers))