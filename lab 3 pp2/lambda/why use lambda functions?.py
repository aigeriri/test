#syntax

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

"22"

#2
def myfunc(n):
    return lambda  a : a * n

 mytripler = myfunc(3)

 print(mytripler(11))

 "33"   

 #3
def myfunc(n):
    return lambda a : a * n

 mydoubler = myfunc(2)
 mytripler = myfunc(3)

 print(mydoubler(11))
 print(mytripler(11))   

 '''
 22
 33
 '''