thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#['banana', 'cherry']



thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".

'''
Traceback (most recent call last):
  File "demo_list_del2.py", line 3, in <module>
    print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
NameError: name 'thislist' is not defined
'''