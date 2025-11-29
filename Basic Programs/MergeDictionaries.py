dict1 = {"a":1, "b":2, "c":3}
dict2 = {"a":2, "d":5, "e":6}

merged = dict1|dict2
dict1.update(dict2)

print(merged)
print(dict1)