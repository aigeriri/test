set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# {'b', 1, 'a', 'c', 2, 3}

#Note: Both union() and update() will exclude any duplicate items.

