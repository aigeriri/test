def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

input_string = "AIko"
upper, lower = count_case(input_string)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
