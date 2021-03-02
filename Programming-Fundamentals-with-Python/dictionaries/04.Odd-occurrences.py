words = input().split()
words_count = {}

for word in words:
    l_word = word.lower()
    if l_word not in words_count:
        words_count[l_word] = 0
    words_count[l_word] += 1

odd_occurrences = [word for word in words_count if not words_count[word] % 2 == 0]
print(*odd_occurrences)
