item_type = "Bags"
customer_name = "Ramesh"


print(f"Order for {customer_name} : {item_type} please  !")

item_description = "Comfortable and Flexible"
print(f"First Word: {item_description[0:8:2]}")
print(f"First Word:{item_description[:8]}")
print(f"Last Word:{item_description[15:]}")
print(f"Last Word:{item_description[::-1]}")

label_text = "Item Special"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded Label : {encoded_label}")
decoded_label  = encoded_label.decode("utf-8")
print(f"Encoded label : {decoded_label}")

