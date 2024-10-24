import re
string = "InsertSpacesBetweenWords"
result = re.sub(r'([A-Z])', r' \1', string)
print(result.strip())
