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
class Dog:
    def __init__(self, name, happiness, hunger, energetic, dirty):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.energetic = energetic
        self.dirty = dirty
    def play(self, happy, game):
        y = input(f"What do you want to play with {self.name}?(fetch, tug of war, hide and seek)")
        if y == "fetch":
            happy = 100
        elif y == "tug of war":
            happy = 60
        elif y == "hide and seek":
            happy = 20
        else:
            print(f"invalid action, you won't be able to feed {self.name} again until tomorrow(sorry)")
        self.game = y
        self.happiness += happy
        print(f"{self.name} played {game} and her happiness is {self.happiness}")




    def show_status(self):
        print(f"{self.name}: {self.__dict__}")



    def sleep(self, energy,):
        z = 0
        y = input(f"where will {self.name} sleep?(bed, chair, floor, lawn)")
        if y == "bed":
            z = 100
        elif y == "chair":
            z = 75
        elif y == "floor":
            z = 50
        elif y == "lawn":
            z = 25
        else:
            print(f"invalid action, {self.name} won't be able to sleep again until tomorrow(sorry)")
            print(f"{self.name} slept on the {y} for {x/10} hours and energy is at {self.energetic}")
        x = int(input(f"how many hours will {self.name} sleep?(1-10)"))
        x *=10
        t = x + z
        t *= 0.5
        energy = t
        self.energetic += energy



    def hunger(self, cals, food):
        self.food = food
        y = input(f"What do you want to feed {self.name}?(chicken, pizza, bread, crackers)")
        self.cals = cals
        if y == "chicken":
            cals = 100
        elif y == "pizza":
            cals = 75
        elif y == "bread":
            cals = 50
        elif y == "cracker":
            cals = 25
        else:
            print(f"invalid action, you won't be able to feed {self.name} again until tomorrow(sorry)")
            self.food = y
        self.hunger += cals
        print(f"you fed {self.name} {self.food} and her hunger is now {self.hunger}")
    
    
    
    def dirty(self, clean, method):
        self.method = method
        x = input(f"How do you want to clean {self.name}?(bath, brush, scrub, shampoo)")
        if x == "bath":
            clean = 100
        elif x == "scrub":
            clean = 75
        elif x == "brush":
            clean = 50
        elif x == "shampoo":
            clean = 25
        else:
            print(f"invalid action, you won't be able to clean {self.name} again until tomorrow(sorry)")
        self.method = x
        self.dirty += clean
        print(f"you {self.method}ed {self.name} and her cleanliness is now {self.dirty} ")

x = input("What do you want to name your dog?")
x = Dog(f"{x}", 100, 100, 100, 100)
x.show_status()


