num = [1,2,2,2,4,3,4,5]

def check_freq():
    freq = {}
    for ch in num:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(f"Frequrncy of list:{check_freq()}")