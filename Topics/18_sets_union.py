s1 = {1, 2, 3, 4, 5} # this is a set, it is unordered and mutable
s2 = {4, 5, 6, 7, 8} # this is another set, it is unordered and mutable

s1.union(s2) # this will return a new set that is the union of s1 and s2

# note : the union of two sets is a set that contains all the elements of both sets, without duplicates
print("union of 2 sets: ", s1.union(s2))

s1.intersection(s2) # this will return a new set that is the intersection of s1 and s2

# note : the intersection of two sets is a set that contains only the elements that are common to both sets
print("intersection of 2 sets: ", s1.intersection(s2))

subset = s1.issubset(s2) # this will check if s1 is a subset of s2, it will return boolean value
print("is s1 a subset of s2: ", subset)

superset = s1.issuperset(s2) # this will check if s1 is a superset of s2, it will return False
print("is s1 a superset of s2: ", superset)

a = s1 - s2 # this will return a new set that contains the elements that are in s1 but not in s2
print("difference of 2 sets: ", a)