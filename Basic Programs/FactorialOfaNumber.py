#Using Recursion
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(6))

#Using for loop

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

result = fact(5)
print(result)