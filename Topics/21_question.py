#write a program to find out weather a studen has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subject and take marks as an input from the user

marks1 = int(input("Enter 1st Marks: "))
marks2 = int(input("Enter 2st Marks: "))
marks3 = int(input("Enter 3st Marks: "))

total = marks1 + marks2 + marks3
percentage = total / 3

if (percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):print("Congratulations! You have passed.")
else:print("Sorry! You have failed.")