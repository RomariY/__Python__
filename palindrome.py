def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def char_check(char):
    forbidden = ('!', ' ', '_', '-', '?', )
    for each in forbidden:
        if char == each:
            return True

something = input('Enter your text: ')
temp = something.lower()

text_miss_space = str()
for char in temp:
    ch = char_check(char)
    if ch:
        continue
    text_miss_space += char

print(text_miss_space)
if (is_palindrome(text_miss_space)):
    print("Yes, " + something + " is palindrome")
else:
    print("No, " + something + " is not a palindrome")