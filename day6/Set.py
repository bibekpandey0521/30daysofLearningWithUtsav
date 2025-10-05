essentails_species = {"cardamom","ginger","cinamon"}
optional_species = {"cloves","ginger", "black pepper"}

all_spices = essentails_species | optional_species
print(f"All Species  : {all_spices}")


common_species = essentails_species & optional_species
print(f"Common Species: {common_species}")

only_in_essential = essentails_species - optional_species
print(f"Only In Essential Species : {only_in_essential}")

print(f"Is 'cloves' in essential speices? {'cloves' in essentails_species} ")
print(f"Is 'cloves' in optional species?  {'cloves' in optional_species}")