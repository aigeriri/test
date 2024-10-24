import re
string = "SplitThisString"
result = re.findall('[A-Z][^A-Z]*', string)
print(result)
