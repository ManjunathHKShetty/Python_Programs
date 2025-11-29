
def largestSmallest(n):
    largest = n[0]
    smallest = n[0]

    for i in range(1, len(n)):
        if largest < n[i]:
            largest = n[i]
        if smallest > n[i]:
            smallest = n[i]

    return largest, smallest

print(largestSmallest([40,10,20,100,30,90]))

# indices and value
def largestSmallest(n):
    largest = n[0]
    smallest = n[0]
    largest_index = 0
    smallest_index = 0

    for i in range(1, len(n)):
        if largest < n[i]:
            largest = n[i]
            largest_index = i
        if smallest > n[i]:
            smallest = n[i]
            smallest_index = i

    return (largest,largest_index), (smallest,smallest_index)

print(largestSmallest([40,10,20,100,30,90]))