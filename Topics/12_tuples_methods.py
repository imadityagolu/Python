a = (1,5,2,8,4,1,"Hello",False) # this is a tuple, it is immutable and ordered
print(a)

# no = a.count(1) # this will count the number of occurrences of 1 in the tuple
print("count: ", a.count(1))

index = a.index(8) # this will return the index of the first occurrence of "Hello" in the tuple
print("index of 8: ", index)

print(7 in a) # this will check if 7 is in the tuple, it will return False