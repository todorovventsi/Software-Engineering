def palindrome(text, index=0):
    right_index = len(text) - 1 - index
    index_diff = index - right_index
    if not text[index] == text[right_index]:
        return f"{text} is not a palindrome"
    if abs(index_diff) <= 1:
        return f"{text} is a palindrome"
    return palindrome(text, index + 1)


print(palindrome("peter", 0))
print(palindrome("abcba", 0))
