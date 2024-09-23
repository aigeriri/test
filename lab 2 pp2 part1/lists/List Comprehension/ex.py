fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

#['apple', 'banana', 'mango']

'''
The Syntax
newlist = [expression for item in iterable if condition == True]
'''


