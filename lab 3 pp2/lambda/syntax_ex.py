#1
x = lambda a: a + 10
print(x(5))

"15"

#2
x = lambda a: a, b: a * b
print(x(5, 6))

"30"

#3
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

"13"
