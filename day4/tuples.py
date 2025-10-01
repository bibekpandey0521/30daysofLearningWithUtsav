fruits = ("apple","mango","orange")

(fruit1,fruit2,fruit3) = fruits

print(f"Fruits are {fruit1},{fruit2},{fruit3}")

item1_ratio , item2_ratio = 2,1
print(f"Ratio of I1 : {item1_ratio} and I2: {item2_ratio}")
item1_ratio , item2_ratio = item2_ratio , item1_ratio
print(f"Ratio of I1 : {item1_ratio} and I2: {item2_ratio}")


#member testing
print(f"Is apple in fruits ? {'apple' in fruits}")