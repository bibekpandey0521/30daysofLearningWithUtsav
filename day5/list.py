#mutable
ingredients = ["water","milk","black tea"]

ingredients.append("sugar")
print(f"Ingredients are {ingredients}")
ingredients.remove("water")
print(f"Ingredients are {ingredients}")


spice_options = ["ginger","cardamom"]
tea_ingredients = ["water","milk"]

tea_ingredients.extend(spice_options)
print(f"Tea: {tea_ingredients}")
tea_ingredients.insert(2,"black tea")

print(f"Tea : {tea_ingredients}")

last_added = tea_ingredients.pop()
print(f"{last_added}")
print(f"Tea : {tea_ingredients}")
tea_ingredients.reverse()
print(f"Tea: {tea_ingredients}")
tea_ingredients.sort()
print(f"Tea: {tea_ingredients}")


sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level :{max(sugar_levels)}")
print(f"Minimum sugar level :{min(sugar_levels)}")