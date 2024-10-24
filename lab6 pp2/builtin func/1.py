from functools import reduce

def multiply_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers_list = [5, 7, 9, 3]
result = multiply_numbers(numbers_list)
print(f"Product of all numbers in the list: {result}")
