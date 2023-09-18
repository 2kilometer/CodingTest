str = input()
words = [word.lower() if word.isupper() else word.upper()
         for word in str]

print("".join(words))