#Ex: [0 1 1 2 3 5 8]

def fib(n):
    sequence = []
    a,b = 0,1

    if n <= 0:
        return "Value should be greater than 0"
    elif n == 1:
        sequence.append(a)
    else:
        sequence.append(a)
        sequence.append(b)

        for i in range(2,n):
            c = a+b
            a = b
            b = c

            sequence.append(c)

    return sequence

print(fib(7))

#Fibonacci limit
def fib_limit(limit):
    a, b = 0,1
    result = []

    while a < limit:
        result.append(a)
        a,b = b,a+b

    return result

print(fib_limit(200))



