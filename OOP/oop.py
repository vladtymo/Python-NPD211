# OOP: incapsulation, inheritance, polymorphism, abstaction

class Order:
    # static fields
    count = 0

    def __init__(self, price, client, quantity = 1):
        Order.count += 1
        self.number = Order.count
        self.price = price
        self.client = client
        self.__quantity = quantity
        
    def __del__(self):
        print(f"Order #{self.number} is deleting...")
    # properies

    # setter & getter
    @property # - decorator for getters
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        if value > 0:
            self.__quantity = value
        else:
            print("Quantity must be greather than 0")

    # methods
    def setQuantity(self, value):
        if value > 0:
            self.__quantity = value

    def getQuantity(self):
        return self.__quantity

    def oneMore(self):
        self.__quantity += 1
    def oneLess(self):
        self.__quantity -= 1

    def __str__(self) -> str:
        return f"Order #{self.number} made by {self.client} - {self.price}$"
    
    # operator '+'
    def __add__(self, other):
        return Order(self.price + other.price, self.client, self.quantity + other.quantity)

order1 = Order(3400, "Vlad Tm")
# order1.client = "Vlad Tm"

print(order1)
# print(f"Order #{order1.number} made by {order1.client} - {order1.price}$")

order2 = Order(6999, "Igor Mar")

print(order2)
order2.oneMore()
order2.oneMore()

# order2.setQuantity(10)
order2.quantity = 10
order2.quantity = -1

# print(order2.getQuantity())
print(order2.quantity)

print(order1 + order2)

