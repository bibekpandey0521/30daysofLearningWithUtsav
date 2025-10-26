class Tea:
    temperature = "Hot"
    strength = "Strong"

# Create an instance of Tea
morning_tea = Tea()

print(morning_tea.temperature)

# Modify instance attributes
morning_tea.temperature = "Mild"
morning_tea.cup = "Small"

print("After changing:", morning_tea.temperature)
print("Cup size is:", morning_tea.cup)
print("Direct look into the class:", morning_tea.temperature)


# del morning_tea.temperature
# del morning_tea.cup
# print(morning_tea.temperature)
# print(morning_tea.cup)
