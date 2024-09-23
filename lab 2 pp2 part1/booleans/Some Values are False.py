print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


'''
False
False
False
False
False
False
False
'''

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

'''
False
'''