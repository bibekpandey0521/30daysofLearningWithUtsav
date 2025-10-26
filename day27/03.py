class TeaCup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml cup Tea"
    
cup = TeaCup()
print(cup.describe())    
print(TeaCup.describe(cup))

cup_two = TeaCup()
cup_two.size = 100
print(TeaCup.describe(cup_two))