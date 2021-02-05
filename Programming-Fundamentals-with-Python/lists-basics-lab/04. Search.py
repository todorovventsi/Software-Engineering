n = int(input())
criteria = input()

all_words = []
matched_words = []

for _ in range(n):
    current_word = input()
    all_words.append(current_word)
    if criteria in current_word:
        matched_words.append(current_word)
print(all_words)
print(matched_words)
