n_of_words = int(input())
synonyms = {}

for _ in range(n_of_words):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")
