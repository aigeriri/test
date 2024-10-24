import re
def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

string = "snake_case_string"
print(snake_to_camel(string))
