tea_order = dict(type="Blend Tea",size="Large",sugar=2)
print(f"Tea order:{tea_order}")

tea_recipe = {}
tea_recipe["base"] = "black tea"
tea_recipe["liquid"] = "milk"

print(f"Recipe base:{tea_recipe['base']}")
print(f"Recipe :{tea_recipe}")
del tea_recipe['liquid']
print(f"Recipe: {tea_recipe}")

print(f"Is sugar in the order? {'sugar' in tea_order}")


tea_order = {"type":"Ginger Tea","Size":"Medium","Sugar":1}

# print(f"Order details (keys): {tea_order.keys()}")
# print(f"Order details (items): {tea_order.values()}")
# print(f"Order details (items): {tea_order.items()}")


last_item = tea_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom":"crushed","ginger":"sliced"}
tea_recipe.update(extra_spices)

print(f"Updated tea recipe:{tea_recipe}")

tea_size = tea_order["Size"]
print(f"Tea Size is {tea_size}")

customer_note = tea_order.get("note", "No Note")
print(f"Tea Size is {customer_note}")
