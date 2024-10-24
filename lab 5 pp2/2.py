import re
pattern = r'ab{2,3}'
string = "abbb"
match = re.match(pattern, string)
print(match)
