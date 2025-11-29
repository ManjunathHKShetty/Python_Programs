arr = [1, 2, 2, 3, 4, 4, 5, 1, 6]

def find_unique_elements():
    unique = []
    freq ={}

    for ch in arr:
        freq[ch] = freq.get(ch, 0) + 1
    for i, j in freq.items():
        if j == 1:
            unique.append(i)

    # unique_ele = [key for key, value in freq.items() if value == 1]

    return unique

find_unique_elements()

print(f"Unique elements are:{find_unique_elements()}")
