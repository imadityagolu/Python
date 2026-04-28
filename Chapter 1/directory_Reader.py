import os

# method 1----------------------------------------------
# directory = os.getcwd()
# print("Current Directory:", directory)

# method 2----------------------------------------------
# '/' is the root directory of systems in which the .py file is.
context = os.listdir('/')
for item in context:
    print(item)