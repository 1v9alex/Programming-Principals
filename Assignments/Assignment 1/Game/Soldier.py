import random

#Creating and initalizing the soldier class

class Soldier:
    def __init__(self, name):
        #Initializing the attributes of the soldier
        self.name = name
        self.gold = 0
        self.health = 50
        self.damage = 2
        self.armor = 1
        self.stamina = 1
        self.questCompleted = False
        self.shopVisited = False
        #Dictionary of items that the soldier has
        self.items = {"Offensive": [], "Defensive": []}
        #List of challenges that the soldier has to complete
        self.challenges = [
            {"name": "Battle your first dragon", "attribute": "damage"},
            {"name": "Invade your first kingdom", "attribute": "stamina"},
            {"name": "Overthrow the evil king", "attribute": "armor"},
            {"name": "Become The King", "attribute": "Damage"}
                        
                        ]
        #Dictionary of items that the shop has for the soldier role
        self.shopItems = {
            "Offensive": {
                "Dragon's Tooth": 10, "Excalibur": 100, "Blade Of Steel": 5, "Blade Of The Fallen": 50, "Long Sword": 30
            },
            "Defensive": {
                "Armour Of The Gods": 80, "Boots Of Quickness": 50, "Iron Armour": 20
            }
        }
        
        def battleDragon(self):
            #Creating the logic for the first challenge, "Battle your first dragon"
            print("While returning from a long journey, you encounter a dragon!")
            
            dragonHealth = 30
            dragon_damage = random.randint(2,12)
            
            while True: #Creating a loop that will run until you choose to battle the dragon
                dragonChoice = input("Do you want to battle the dragon? (y/n): ").lower()
                
                if dragonChoice in {'y','yes'}:
                    print("You have chosen to battle the dragon!")
                    while self.health > 0 and dragonHealth > 0:
                        print("You angered the dragon, and it attacks you!")
                    
                    print("Luckily You dodged its attack, what will you do now?")
                    print(f"Your health: {self.health}, Dragon's health: {dragonHealth}")

                    choice = input("Do you want to 1) Attack or 2) Defend")
                    die1 = random.randint(1,6)
                    die2 = random.randint(1,6)
                    numRolled = die1 + die2
                    criticalStrike = die1 == die2
                    
                    if criticalStrike:
                        print("Critical Strike!")
                        
                    if choice == '1': #Attack
                        print(f"You decide to attackthe dragon!, you rolled a {numRolled}")
                        dragonAction = random.choice(['dodge', 'defend'])
                        
                        if dragonAction == 'dodge':
                            if numRolled < 6:
                                print("The Dragon dodged your attack!")
                            else:
                                print("You hit the dragon!")
                                damage = numRolled + (2 if criticalStrike else 0)
                                dragonHealth -= damage
                        else:
                            print("The dragon defended your attack!, You will deal reduced damage")
                            damage = numRolled + (2 if criticalStrike else 0) - 1
                            dragonHealth -=  max(damage - dragonHealth, 0)
                    
                    elif choice == '2': #Defend
                        print("You decide to defend against the dragon!")
                        dragonAttack = random.randint(1,6) + random.randint(1,6)
                        if dragonAttack > 6:
                            print("The dragon hit you!")
                            damage = dragonAttack - self.armor
                            self.health -= max(damage - self.health, 0)
                        else:
                            print("The dragon missed!")
                            
                    if dragonHealth <= 0:
                        print("You have defeated the dragon!")
                        self.challenges.remove({"name": "Battle your first dragon", "attribute": "damage"})
                        self.damage += 2
                        self.gold += 30
                        break
                        print("You have gained 30 gold!")
                    elif self.health <= 0:
                        print("You have been defeated by the dragon!")
                        print("GAME OVER")
                        break
                        
                    break
                elif dragonChoice in {'n','no'}:
                    print("You remember the kings words, \"I became king because I never backed down from a challenge\"")
                else:
                    print("Invalid Input. Please Enter 'y', 'yes', 'n', or 'no'")