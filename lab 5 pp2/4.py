import re
pattern = r'[A-Z][a-z]+'
string = "Abc"
match = re.match(pattern, string)
print(match)
