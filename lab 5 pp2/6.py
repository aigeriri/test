import re
string = "Hello, world. How are you?"
result = re.sub(r'[ ,.]', ':', string)
print(result)
