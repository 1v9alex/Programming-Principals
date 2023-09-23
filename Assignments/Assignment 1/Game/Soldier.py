import random

#Creating and initalizing the soldier class

class Soldier:
    def __init__(self, name):
        #Initializing the attributes of the soldier
        self.name = name
        self.gold = 10
        self.health = 50
        self.damage = 2
        self.armor = 1
        self.stamina = 1
        self.questCompleted = False
        self.shopVisited = True
        self.questsCompletedCount = 0
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
        
        inBattle = False
            
        while True: #Creating a loop that will run until you choose to battle the dragon
            if not inBattle:
                dragonChoice = input("Do you want to battle the dragon? (y/n): ").lower()
                    
                if dragonChoice in {'n','no'}:
                    print("You remember the kings words, \"I became king because I never backed down from a challenge\"")
                    continue #skips to the next iteration of the loop asking the user again
                elif dragonChoice not in {'y','yes'}:
                    print("Invalid Input. Please Enter 'y', 'yes', 'n', or 'no'")
                    continue #skips to the next iteration of the loop asking the user again
                
                inBattle = True
                
                #Battle logic
                while self.health > 0 and dragonHealth > 0:
                    dragonDamage = random.randint(1,6) + random.randint(1,6)
                    
                    print(f"Your health: {self.health}, Dragon's health: {dragonHealth}")

                    choice = input("Do you want to 1) Attack or 2) Defend")
                    die1 = random.randint(1,6)
                    die2 = random.randint(1,6)
                    numRolled = die1 + die2
                    criticalStrike = die1 == die2
                    
                    if criticalStrike:
                        print("Critical Strike!")
                        
                    if choice == '1': #Attack
                        print(f"You decide to attack the dragon!, you rolled a {numRolled}")
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
                        print("You have gained 30 gold!")
                        self.questCompleted = True
                        self.shopVisited = False
                        self.questsCompletedCount += 1
                        break
                    elif self.health <= 0:
                        print("You have been defeated by the dragon!")
                        print("GAME OVER")
                        break
                if inBattle:
                    break
    
    def invadeKingdom(self):
        if 1 > 3:
            print("You have not completed the previous challenges yet!")
            return
        
    
    def overthrowKing(self):
        if 1 > 2:
            print("You have not completed the previous challenges yet!")
            return
        
    
    def becomeKing(self):
        if 1 > 1000:
            print("You have not completed the previous challenges yet!")
            return
        
    def visitShop(self):
        if self.questsCompletedCount <= 0 or (self.questsCompletedCount <= len(self.challenges) and self.shopVisited):
            print("You cant visit the shop now!")
            return
        
        while True:
            print("\nWelcome to the shop!")
            print("You Currently Have:", self.gold, "gold")
            print("\nAvailable Items:")
                
            print("Offensive Items:")
            for item, cost in self.shopItems["Offensive"].items():
                print(f"{item}: {cost} gold")
                
            print("\nDefensive Items:")
            for item, cost in self.shopItems["Defensive"].items():
                print(f"{item}: {cost} gold")
                
            itemToBuy = input("\nWhat would you like to buy? (Type 'exit' to exit): ").title()
            
            if itemToBuy == 'exit':
                break
            
            foundItem = None
            itemType = None
            
            #Checking if the item exists in the shop
            for itype, items in self.shopItems.items():
                if itemToBuy in items:
                    foundItem = itemToBuy
                    itemType = itype
                    break
            
            if foundItem:
                if self.gold >= self.shopItems[itemType][foundItem]:
                    #deduct the gold from the player and then add the item to the player's inventory
                    self.gold = self.gold - self.shopItems[itemType][foundItem]
                    self.items[itemType].append(foundItem)
                    print(f"You have bought {foundItem} for {self.shopItems[itemType][foundItem]} gold!")
                else:
                    print("You don't have enough gold!")
            else:
                print("Invalid item name. Please type the exact name of the item!")
            
            self.shopVisited = True

    def startNextQuest(self):
        if self.questsCompletedCount == 0:
            print("You have not completed any quests yet!")
            #if no quests are completed the player is then able to start the first quest
            self.battleDragon() #starting the first quest
            
        elif self.challenges: #checking if there are still challenges remaining
            challenge = self.challenges[0] # getting the next challenge
            challengeName = challenge["name"]
            print(f"\nStarting quest: {challengeName}")
            
            #Checking if the player is allowed to visit the shop before starting the quest
            if not self.shopVisited and self.questsCompletedCount > 0:
                self.visitShop()
            
            
            #Adding the logic for the next quests
            if challengeName == "Invade your first kingdom":
                self.invadeKingdom()
            elif challengeName == "Overthrow the evil king":
                self.overthrowKing()
            elif challengeName == "Become The King":
                self.becomeKing()
                
            
            #Update questsCompleteCount and reseting the value of shopVisited after completing a quest
            self.questsCompletedCount += 1
            self.shopVisited = False
            
        else:
            print("You have completed all the quests!, You are the new king!")


