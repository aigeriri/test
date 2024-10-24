import re
pattern = r'a.*b$'
string = "a123b"
match = re.match(pattern, string)
print(match)
