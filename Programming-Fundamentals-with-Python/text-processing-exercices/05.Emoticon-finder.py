text = input()

# emoticons = [item for item in text if ":" in item]
emoticons = [f"{text[index]}{text[index + 1]}" for index in range(len(text)) if text[index] == ":"]

print('\n'.join(emoticons))