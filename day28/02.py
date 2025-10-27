class TeaOrder:

    def __init__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} Tea."

order  = TeaOrder("Mix",200)
print(order.summary())

order_two = TeaOrder("Ginger",200)
print(order_two.summary())