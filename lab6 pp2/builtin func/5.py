def all_elements_true(tup):
    return all(tup)

input_tuple = (True, True, False)
result = all_elements_true(input_tuple)
print(f"Are all elements true? {result}")
