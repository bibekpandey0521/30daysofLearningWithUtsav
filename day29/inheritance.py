## Inheritance
## Parent class
class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype
    def drive(self):
        print(f"The person will drive the {self.enginetype} car ")

car1 = Car(4,5,"petrol")
car1.drive()


class Tesla(Car):
    def __init__(self, windows, doors, enginetype,is_selfdriving):
        super().__init__(windows,doors,enginetype)
        self.is_selfdriving= is_selfdriving

    def selfdriving(self):
        print(f"Tesla supports self driving:  {self.is_selfdriving}")

tesla1 = Tesla(4,5,"electric",True)
tesla1.selfdriving()

tesla1.drive()