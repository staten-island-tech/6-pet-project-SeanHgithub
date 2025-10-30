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
    def __init__(self, name, happiness, hunger, energetic, dirty):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.energetic = energetic
        self.dirty = dirty
    def play(self, happy, game):
        self.happiness += happy
        print(f"{self.name} is playing {game}")
    def show_status(self):
        print(f"{self.name}'s happiness is now {self.happiness}")
    def sleep(self, energy):
        x = int(input(f"how many hours will {self.name} sleep?(1-10)"))
        x *=10
        energy = x
        self.energetic += energy
    def hunger(self, food):
        x = int(input(f"how many calories do you want to feed {self.name}(50-500)"))
        x %= 5 
        food = x
        self.hunger += food
    def dirty(self, clean, method):
        self.dirty += clean
        print(f(""))

Snowball = Pet("Snowball", 67)
Snowball.play(20, "fetch")
Snowball.show_status()

