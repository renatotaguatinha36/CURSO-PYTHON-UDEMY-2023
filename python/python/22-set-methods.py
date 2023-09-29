# 1. Add, Remove and Discard
my_set = {10, 2, 10, 5, 7}

print(my_set)
my_set.add(8)
print(my_set)
# my_set.remove(200)  # Error if element is absent
my_set.discard(200)  # No Error if element is absent
print(my_set)


# 2. Intersection and Union
my_set = {10, 2, 10, 5, 7}
other_set = {34, 1, 10, 5}

print(my_set.intersection(other_set))
print(other_set.intersection(my_set))
print(my_set.intersection((2, 100, 200)))
print(my_set & other_set)

print(my_set.union(other_set))
print(other_set.union(my_set))
print(my_set.union(other_set) == other_set.union(my_set))
print(my_set | other_set)


# 3. Copy
my_set = {10, 2, 10, 5, 7}
other_set = {34, 1, 10, 5}

set_copy = other_set.copy()
set_copy.add(200)
print(set_copy)
print(other_set)


# 4. Issubset and Issuperset
my_set = {10, 5}
other_set = {34, 1, 10, 5}

print(my_set.issubset(other_set))
print(other_set.issuperset(my_set))


# 5. Symmetric Difference
a = {'a', 'c', 'd'}
b = {'l', 'm', 'c'}

print(a.symmetric_difference(b))

print((a | b) - (a & b))
