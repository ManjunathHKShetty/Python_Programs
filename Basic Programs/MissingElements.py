arr = [1, 2, 4, 5, 9, 12]
missing = []

def find_missing_elements():
    for i in range(arr[0], arr[-1]+1):
        if i not in arr:
            missing.append(i)
    return missing

print(f"Missing Elements in the array:{find_missing_elements()}")