info = {
    "Name": "John",
    "Address": "123 Street",
    "Pin": 1234,
    "Marks": [90, 80, 85, 95, 88],
    0: "Male"
}

info.update({"Phone": 1234567890}) # this will add a new key-value pair to the dictionary
info.update({"Name": "Aditya"}) # this will update the value of the key "Name" to "Aditya"
print(info.items())