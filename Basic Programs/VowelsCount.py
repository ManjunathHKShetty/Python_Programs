def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(f"Vowels Count:{count_vowels('Hello world I am alive')}")

def count_individual_vowels(s):
    vowels = "aeiouAEIOU"
    vowels_count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for char in s.lower():
        if char in vowels:
            vowels_count[char] += 1
    return vowels_count

print(f"Vowels Count:{count_individual_vowels('Hello world I am alive')}")