a = set() # this is an empty set, it is unordered and mutable
print(type(a))

sets = {1, 2, 3, 4, 5} # this is a set, it is unordered and mutable
print(type(sets))

b = {1, 2, 3, 4, 5, 1, 2} # this is a set, it will remove duplicate values, as set dont allow duplicate values
print(b)