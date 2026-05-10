mark = []

m1 = int(input("Enter 1s mark: "))
mark.append(m1)
m2= int(input("Enter 2s mark: "))
mark.append(m2)
m3 = int(input("Enter 3s mark: "))
mark.append(m3)
m4 = int(input("Enter 4s mark: "))
mark.append(m4)
m5 = int(input("Enter 5s mark: "))
mark.append(m5)

mark.sort() # this will sort the list in ascending order

add = sum(mark) # this will calculate the sum of all the marks in the list

top = mark.count(100) # this will count the number of occurrences of 100 in the list

print("Marks: ", mark)
print("Sum: ", add)
print("Average: ", add/5) # this will calculate the average of the marks
print("Number of 100s: ", top)