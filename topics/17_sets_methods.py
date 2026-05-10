s = {1, 4, 3, "Aditya", 2, 5}

s.add(6) # this will add 6 to the set
print("add (add 6 to the set): ", s)

s.remove(3) # this will remove 3 from the set
print("remove (remove 3 from the set): ", s)

s.discard(7) # this will remove 7 from the set, if 7 is not present in the set, it will not raise an error
print("delete (remove 7 from the set): ", s)

s.pop() # this will remove and return an arbitrary element from the set
print("pop (remove and return an arbitrary element from the set): ", s)

# this will return the number of elements in the set
print("length of the set: ", len(s))

s.clear() # this will remove all the elements from the set
print("clear (remove all the elements from the set): ", s)