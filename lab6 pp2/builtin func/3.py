def is_palindrome(s):
    return s == s[::-1]

input_string = "aziza"
result = is_palindrome(input_string)
print(f"Is '{input_string}' a palindrome? {result}")
