import re
pattern = r'ab*'
string = "abbbb"
match = re.match(pattern, string)
print(match)
