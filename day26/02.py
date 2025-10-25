class School:
    location = "ktm"

print(School.location)

School.is_holiday = True

# Creating object from class School
s1 = School()
print("School", s1.location)
print("School", s1.is_holiday)

s1.is_Vacation = False
print("Class:", getattr(School, "is_Vacation", "Attribute not found"))
