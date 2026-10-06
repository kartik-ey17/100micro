from dataclasses import dataclass,field
import random

@dataclass
class survivalGame:
    health: int = 100
    food: int = 100
    water: int = 100
    energy: int = 60
    day: int = 1
    shelter: bool = False
    inventory: set[str] = field(default_factory=lambda: {"tire", "oil"})

    def changeResource(self , field_name , change):
        curr = getattr(self , field_name)
        setattr(self , field_name , max(0, min(100 , curr + change)))

    def display(self):
        print(f"+=+=+= DAY {self.day} =+=+=+\nHealth: {self.health}/100\nFood: {self.food}/100\nWater: {self.water}/100\nEnergy: {self.energy}/100\nItems: {', '.join(self.inventory) if self.inventory else 'None'}\nShelter: {'Built' if self.shelter else 'Not built yet.'}")

    def luckRoll(self):
        return random.randint(1,100)

    def dayEnd(self):
        luck = self.luckRoll()
        if luck < 30 and not self.shelter:
            self.changeResource("energy" , -25)
            self.changeResource("health" , -25)
            print(f"Tonight was cold! You were without shelter. The night drained your energy and health. Making shelter is recommended.")

        if self.food == 0:
            self.changeResource("health" , -10)
            self.changeResource("energy" , -10)
            print("You are starving bro!")
        if self.water == 0:
            self.changeResource("health" , -20)
            self.changeResource("energy" , -10)
            print("Your dehydrated son!")
        if self.energy == 0:
            self.changeResource("health" , -15)
            print("Your exhausted! get some rest")

        self.changeResource("food" , -10)
        self.changeResource("water" , -10)
        self.day += 1

    def actions(self , choice):
        luck = self.luckRoll()
        if choice == 1:
            if luck == 100:
                self.changeResource("food" , 40)
                self.changeResource("water" , 30)
                print("Nice luck broski! you immediately found 40 food with 30 water and did not even loose any energy.")

            elif luck > 70:
                self.changeResource("food" , 30)
                self.changeResource("water" , 20)
                self.changeResource("energy" , -10)
                print(f"Found 30 food and 20 water. 10 energy drained")

            elif luck > 40:
                self.changeResource("food" , 15)
                self.changeResource("water" , 10)
                self.changeResource("energy" , -15)
                print("Found 15 food , 10 water on a loss of 15 energy!")
            else:
                self.changeResource("food" , 10)
                self.changeResource("water" , 10)
                self.changeResource("energy" , -20)
                print(f"Found 10 food and 10 water. 20 energy drained")
        elif choice == 2:
            if "medicine" in self.inventory and self.health < 70:
                self.inventory.remove("medicine")
                self.changeResource("health" , 30)
                print("Used meds to recover +30 health")
            if luck == 100:
                self.changeResource("energy" , 60)
                print("You had a very nice rest ! +60 energy")
            elif luck > 70:
                self.changeResource("energy" , 35)
                print("You had a good rest ! + 35 energy")
            elif luck > 40:
                self.changeResource("energy" , 25)
                print("You had a rest ! +25 energy")
            else:
                self.changeResource("energy" , 10)
                print("You had a bad nightmare still you managed to rest somehow! +10 energy")
        elif choice == 3:
            self.changeResource("energy" , -20)
            itemsFound = ["matchsticks" , "medicine" , "stick"]
            unFound = [i for i in itemsFound if i not in self.inventory]
            if unFound and luck>60:
                item = random.choice(unFound)
                self.inventory.add(item)
                print(f"Successfull exploration! Item found : {item}")
            else:
                print("Better luck next time son!")

        elif choice == 4:
            if not self.shelter:
                self.shelter = True
                self.changeResource("energy" , -30)
                print("Now you have something over your head!")
            else:
                print("Its already there son")

    def events(self):
        luck = self.luckRoll()
        if luck > 80:
            self.changeResource("water" , 25)
            print("It's raining! + 25 water")
        elif luck > 70:
            self.changeResource("food" , 25)
            print("A helicopter noticed you and sent food supplies! + 25 food")
        elif luck < 30:
            self.changeResource("health" , -20)
            print("Got an injury during the day! -20 health")

def main():
    game = survivalGame()

    while game.day <= 10 and game.health > 0:
        game.display()

        print("\nWhat will you do?\n1. Search for food and water\n2. Rest\n3. Explore\n4. Make a shelter")

        try:
            choice = int(input("\nChoice : "))
            if choice not in range(1,5):
                continue
        except ValueError:
            continue

        event = game.actions(choice)
        game.events()
        game.dayEnd()
    print("---------------------")
    if game.health > 0:
        print("SURVIVAL SUCCESSFUL!")
    else:
        print("GAME OVER!")

main()