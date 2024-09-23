thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist)

#['Kiwi', 'Orange', 'banana', 'cherry']


thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)

#['banana', 'cherry', 'Kiwi', 'Orange']