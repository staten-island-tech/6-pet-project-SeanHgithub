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
    def __init__(self, name, happiness, hunger, energetic, dirty, day):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.energetic = energetic
        self.dirty = dirty
        self.day = day
        self.alive = True
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



    def sleep(self, energy, day):
        z = 0
        self.day = day
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
        day += 1

    def hunger(self, cals, food):
        self.food = food
        y = input(f"What do you want to feed {self.name}?(chicken, peanut butter, bread, crackers)")
        self.cals = cals
        if y == "chicken":
            cals = 100
        elif y == "peanut butter":
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
    def death(self, reason):
         print(f"You let {self.name} die from {reason} after {self.day} day(s)")
    def check_death(self):
        if self.hunger == 0:
            self.death("starvation")
        elif self.dirty == 0:
            self.death("filthy")
        elif self.happiness == 0:
            self.death("depression")
        elif self.energetic == 0:
            self.death("sleep deprivation")
    def Day_1(self):
        y = False
        while y == False:
            y = input(f"where will {self.name} sleep?(bed, chair, floor, lawn)")
            if y == "bed":
                print(f"{self.name} slept very good, great job.")
                y = True
            elif y == "chair":
                print(f"{self.name} slept well, good job.")
                y = True
            elif y == "floor":
                print(f"{self.name} slept ok, but if it keeps up, there will be consequences.")
                y = True
            elif y == "lawn":
                self.death("Freezed")
                y = True
            else:
                print("Invalid response, try again. (bed, chair, floor, lawn)")
        
        y = False
                
    def check_win(self):
        if self.day == 20 and self.alive == True:
            print(f"{self.name} survived for 2 weeks and is ready to go to the vet. CONGRATULATIONS!")
    def background(self):
        story = input("You found a stray dog in the freezing rain and took it in. You must foster her over the next two weeks by feeding, cleaning, and playing with the dog, as well as giving it a place to sleep. Do you accept this challenge?")
        if story.lower == "yes":
            print("........Boom!, the door slams behind you as you bring her in, day 1 begins......")
        elif story.lower == "no":
            print("Ok, if you must.")
        else:
            print("Sorry, try again.(yes/no)")
            input(story)



x = input("What do you want to name your new dog?")
x = Dog(f"{x}", 0, 0, 0, 0, 0)
x.Day_1()