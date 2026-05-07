a = [2, 1, 8, 4]

a.sort() # this will sort the list in place
print("sort: ", a)

a.reverse() # this will reverse the list in place
print("reverse: ", a)

a.append(10) # this will add 10 to the end of the list
print("append (add 10 in last): ", a)

a.insert(2, 5) # this will insert 5 at index 2
print("insert (add 5 at index 2): ", a)

a.remove(1) # this will remove the first occurrence of 1 from the list
print("remove (remove first occurrence of 1): ", a)

a.pop() # this will remove the last item from the list and return it
print("pop (remove last item): ", a)

a.pop(2) # this will remove the item at index 2 and return it
print("pop (remove item at index 2): ", a)

