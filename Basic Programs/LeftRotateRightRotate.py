def left_rotate(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

def right_rotate(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

print(f"Left rotate by 3:{left_rotate([1,2,3,4,5,6],3)}")
print(f"Right rotate by 2:{right_rotate([1,2,3,4,5,6], 2)}")