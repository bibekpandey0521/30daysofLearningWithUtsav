shopping_List = ["Milk","Eggs","Bread"]
print(shopping_List[2])


shopping_List.append("Butter")
shopping_List.insert(1,"Juice")

# print(shopping_List)

# shopping_List.remove("Bread")
# # print(shopping_List)

# shopping_List.pop(0)
# print(shopping_List)

for item in shopping_List:
    print(f"- {item}")

for index, item in enumerate(shopping_List):
    print(f"{index + 1} . {item}")
