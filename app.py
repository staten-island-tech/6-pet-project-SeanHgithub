""" class Calculator():
    def add(x, y):
        print(x + y)
        return x + y
    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)

    def subtract(numbers):
        return numbers

Calculator.add_many([4,32,6,9,214]) """
""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self,item):
        self.inventory.append(item)
        print(self.inventory)
Sean = Hero("Sean", 600, ["Sword"])
Sean.buy("Axe")
print(Sean.__dict__) """
class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.happiness = happiness
    def play(self, happy, game):
        self.__happiness += happy
        
    def show_status(self):
        print(f"{self.name}'s happiness is now {self.__happiness}")
Snowball = Pet("Snowball", 67/100)

