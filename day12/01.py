my_dict = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
}

contact = {
    "name"  : "Joh Doe",
    "phone" : "123-456-789",
    "email" : "john@example.com"
}

print(contact["name"])
print(contact.get("email"))

contact["phone"] = "9807-123-4563"

print(contact.get("email"))

contact["phone"] = "980-123-4563"

print(contact)

contact["address"] = "123 Main St"

print(contact)

del contact["email"]

print(contact)

for key,value in contact.items():
    print(f"{key}: {value}")

if "email" in contact:
    print("Email found")
else:
    print("Email not found")        