class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")
        result = ""
        for char in self.text:
            ascii_number = ord(char) + other
            while ascii_number < 32:
                ascii_number += 95
            while ascii_number > 126:
                ascii_number -= 95
            result += chr(ascii_number)
        return result

some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))
example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))
