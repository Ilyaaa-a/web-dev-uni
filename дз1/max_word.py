with open('example.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words = []
current_word = ''

for char in text:
    if char.isalpha():
        current_word += char
    else:
        if current_word:
            words.append(current_word)
            current_word = ''

if current_word:
    words.append(current_word)

if not words:
    exit()

max_len = max(len(word) for word in words)

for word in words:
    if len(word) == max_len:
        print(word)