def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

# Test
word = "madam"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")    