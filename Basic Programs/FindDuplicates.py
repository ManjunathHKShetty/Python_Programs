#EX:[1,3,3,2,1,5,4]

def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for i in lst:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)

    return list(duplicates)

print(f"Duplicates in [1,3,3,2,2,1,5,4]:{find_duplicates([1,3,3,2,2,1,5,4])}")

