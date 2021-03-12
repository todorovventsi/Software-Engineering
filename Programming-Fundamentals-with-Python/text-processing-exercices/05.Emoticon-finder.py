text = input().split()

# emoticons = [item for item in text if ":" in item]
emoticons = list(filter(lambda x: ":" in x, text))
for emo in emoticons:
    print(emo[:2])