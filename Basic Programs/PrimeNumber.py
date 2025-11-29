#EX: [1,3,5,7,11,13,17,19,23,27,29]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(9))

#or

num = int(input("Enter a value:"))

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")