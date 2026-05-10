info = {
    "Name": "John",
    "Address": "123 Street",
    "Pin": 1234,
    "Marks": [90, 80, 85, 95, 88],
    0: "Male"
}

print(info.items()) # this will print all the key-value pairs in the dictionary as a list of tuples

print(info.keys()) # this will print all the --keys-- in the dictionary as a list

print(info.values()) # this will print all the values in the dictionary as a list

print(info["Name"]) # this will print the value of the key "Name"
print(info.get("Name")) # this will also print the value of the key "Name", but it will return None if the key is not found instead of raising an error
print(info.get("Age")) # this will return None because the key "Age" is not present in the dictionary, but it will not raise an error like info["Age"] would

print(info["Marks"]) # this will print the value of the key "Marks"

print(info[0]) # this will print the value of the key 0