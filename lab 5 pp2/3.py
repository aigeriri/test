import re
pattern = r'[a-z]+_[a-z]+'
string = "abc_def"
match = re.match(pattern, string)
print(match)
