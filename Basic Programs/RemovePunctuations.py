def removePunctuation(t):
    punctuations = "!?',;:.\"-()[]{}<>@#$%^&*_+=/\\|`~"

    cleaned = ""

    for char in t:
        if char not in punctuations:
            cleaned += char
    return cleaned

print(removePunctuation("He&()*)__ll%$^&o! Worl&((d"))