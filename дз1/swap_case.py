s = input().strip()


new = ''

for letter in s:
    if letter.islower():
        new += letter.upper()
    elif letter.isupper():
        new += letter.lower()
    else:
        new += letter

print(new)

