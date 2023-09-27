import random
import string
import time

#Creating and initializing the pickpocket class
class Pickpocket:
    def __init__(self,name,game):
        #Initializing the attributes of the pickpocket
        self.name = name
        self.game = game
        self.gold = 5
        self.health = 5
        self.stealth = 5
        self.luck = 3
        self.speed = 3
        self.questCompleted = False
        self.shopVisited = True
        self.questsCompletedCount = 0
        
        #Dictionary Of Items that the Pickpocket has
        self.items = {"Tools": [], "Utility": []}
        self.inventoryDetails = {"Tools": [], "Utility": []}
        
        #Dictionary of items that the shop has for the pickpocket
        self.shopItems = {
            "Tools": {
                "Developer Item": {"cost": 10000, "stats": {"stealth": 100000, "luck": 100000, "speed": 100000, "health": 100000}},
                "Lockpicking Kit": {"cost": 50, "stats": {"stealth": 2, "luck": 1}}, "Extendo Arm": {"cost": 100, "stats":{"stealth": 12,"luck": 1, "speed": 5}},
                "Alien X-Ray Scanner": {"cost": 150, "stats": {"stealth": -1, "luck": 20, "speed": 10}}, "Silent Wrench": {"cost": 60, "stats": {"stealth": 5, "luck": 1, "speed": 2}},
                
            },
            "Utility": {
                "Item Pouch": {"cost": 0, "stats": {"stealth": 1, "luck": 1, "speed": 1, "health": 1}},
                "Cloak Of Invisibility": {"cost": 100,"stats": {"stealth": 20, "health":10}},
                "Boots Of Swiftness": {"cost": 30,"stats": {"speed": 20, "health":10}},
                "Lucky Charm": {"cost": 20,"stats": {"luck": 10, "health":1, "stealth": -2, "speed": -2}},
                "Secret Camera": {"cost": 50,"stats": {"luck": 5, "stealth": 5, "speed": 5}},
            }
        }
        
        #Challenges that the pickpocket has to complete
        self.challenges = [
            {"name": "Commit your first robbery","attribute": "luck"},
            {"name": "Museum Robbery","attribute": "speed"},
            {"name": "Royal Relic Robbery","attribute": "stealth"},
            {"name": "Steal The Kings Crown","attribute": "stealth"},
        ]
    
    #Creating the function for the first challenge/quest
    def stealFromPasserby(self):
        #Dictionary of victims that the pickpocket can steal from along with the item name, difficulty, and value
        victims = {
            "Blacksmith": {"item": "Newly Forged Iron Sword", "difficulty": 5, "value": 20},
            "Working Man": {"item": "Sack Of Gold Coins", "difficulty": 5, "value": 15},
            "Mage": {"item": "Ancient Scroll", "difficulty": 7, "value": 40},
            "Princess": {"item": "Diamond Necklace", "difficulty": 10, "value": 120},
            "Priest": {"item": "Cleansing Scepter", "difficulty": 9, "value": 60},
        }
        #Initializing the total gold value and stat increment for the items stolen
        totalGoldValue = 0
        statIncrement = 1
        
        #Main loop for stealing
        while True:
            #Printing available victims
            time.sleep(1)
            print("\nYou find yourself in a crowded market, your eyes are scanning for potential victims...")
            
            for i, (victim, info) in enumerate(victims.items(), 1):
                time.sleep(1)
                print(f"{i}. {victim} with {info['item']}")
                
            time.sleep(1)
            #Asking the user to choose a victim
            choice = input("Who will you attempt to steal from? (Enter a number 1-5 or 'exit' to exit) ")
            time.sleep(1)
            
            if choice.lower() == 'exit':
                #Exit the challenge if the player chooses exit
                time.sleep(1)
                print("You decide to leave the market...\nMaybe you will come back later")
                time.sleep(1)
                exit()
            #Validating the users input
            if not (choice.isdigit() and 1 <= int(choice) <= len(victims)):
                print("Invalid choice!")
                continue
            #Getting the chosen victim and difficulty level
            victim = list(victims.keys())[int(choice) - 1]
            difficulty = victims[victim]["difficulty"]
            
            #Asking the user how they would like to attempt the robbery
            time.sleep(1)
            print("\nHow would you like to approach this?")
            time.sleep(1)
            print("1. Distract the victim and then steal the item")
            time.sleep(1)
            print("2. Try to steal the item quietly without the victim noticing")
            time.sleep(1)
            print("3. Try to steal the item quickly and run away")
            time.sleep(1)
            approachChoice = input("Enter your choice (1-3): ")
            time.sleep(1)
            
            #Modifying diffuclty based on the users choice and then printing the corresponding message
            if approachChoice == '1':
                difficulty -= self.luck // 10
                time.sleep(1)
                print("You try to distract the victim...")
            elif approachChoice == '2':
                difficulty -= self.stealth // 10
                time.sleep(1)
                print("You try to steal the item quietly...")
            elif approachChoice == '3':
                difficulty -= self.speed // 10
                time.sleep(1)
                print("You try to snatch the item quickly and run away...")
            else:
                #Continuing the loop if the user enters an invalid choice
                print("Invalid choice!")
                continue
            #Roll dice to determine the sucess of the robbery
            numRolled = random.randint(1, 6) + random.randint(1, 6)
            
            itemName = victims[victim]['item']  # Store item name before deleting
            if numRolled + self.stealth // 10 >= difficulty:
                time.sleep(1)
                print(f"Success! You stole {itemName} from {victim}!")
                totalGoldValue += victims[victim]["value"]
                del victims[victim]

                # Incrementing the stats after successfully stealing
                self.luck += statIncrement
                self.stealth += statIncrement
                self.speed += statIncrement
                statIncrement += 1

                if len(victims) == 0:
                    #End the stealing process if the user has successfully stolen from all the victims
                    time.sleep(1)
                    print("One by one, you've stolen all the victims belongings!")
                    break

                #Giving the player the option to continue or run away
                time.sleep(1)
                print("Nobody noticed you stealing the item! You still feel the adrenaline pumping within you!")
                time.sleep(1)
                action = input("Press 'r' to run away or any other key to continue: ")
                if action.lower() == 'r':
                    #Exit the stealing loop if the player chooses to run away
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("You run away from the market")
                    break
            else:
                #Handling the case where the player fails to steal from the victim
                time.sleep(1)
                print(f"You were Caught! The {victim} noticed your attempt to steal the {itemName}!")
                time.sleep(1)
                retry = input("Your heart is racing! Will you try again? (yes/no): ").lower()
                if retry != 'yes':
                    time.sleep(1)
                    print("You decide it’s time to give up on your criminal desires.")
                    exit()
        time.sleep(1)
        #Updating the players gold and stats after stealing
        print(f"Having escaped, you find that your loot is worth {totalGoldValue} gold!")
        self.gold += totalGoldValue
        time.sleep(1)
        print(f"You gained {totalGoldValue} gold!")
        self.luck += 2
        self.stealth += 1
        self.speed += 1
        self.challenges.remove({"name": "Commit your first robbery", "attribute": "luck"})
        self.questCompleted = True
        self.shopVisited = False
        self.questsCompletedCount += 1

        
            
            
            
            
            
    
    def stealFromMuseum(self):
        return True
    
    def royalRelicRobbery(self):
        return True
    
    def stealKingsCrown(self):
        return True
    
    #Creating the function for the item shop
    def visitShop(self):
        #Check if the player is able to visit the shop based on quest completion and if they have already visited the shop
        if self.questsCompletedCount <= 0 or (self.questsCompletedCount <= len(self.challenges) and self.shopVisited):
            print("You cant visit the shop now!")
            return
        
        
        while True:
            #Printing welcome message and the players gold amount
            print("\nWelcome to the shop!")
            print("You Currently Have:", self.gold, "gold")
            time.sleep(2)
            #Display Tools
            print("Tools:")
            for itemName, itemDetails in self.shopItems["Tools"].items():
                print(f"{itemName}: {itemDetails['cost']} gold")
            #Display Utility Items
            print("\nUtility Items:")
            for itemName, itemDetails in self.shopItems["Utility"].items():
                print(f"{itemName}: {itemDetails['cost']} gold")
            #Prompt user to buy an item or to exit
            itemToBuy = input("\nWhat would you like to buy? (Type 'exit' to exit): ").title()
            formattedInput = itemToBuy.strip().lower().translate(str.maketrans('', '', string.punctuation))
            
            #if the user types exit we exit the shop
            if formattedInput == 'exit':
                break
            
            foundItem = None
            itemType = None
            
            
            #Checking if the item exists in the shop based on the users input
            for itype, items in self.shopItems.items():
                for item in items:
                    formattedItem = item.lower().translate(str.maketrans('', '', string.punctuation))
                    if formattedInput == formattedItem:
                        foundItem = item
                        itemType = itype
                        break
                if foundItem:
                    break
            
            if foundItem:
                #Checks to see if the player has enough gold to buy the selected item
                itemCost = self.shopItems[itemType][foundItem]["cost"]
                if self.gold >= itemCost:
                    #Remove gold from the player, update inventory and stats, and remove the item from the shop
                    self.gold -= itemCost
                    self.inventoryDetails[itemType][foundItem] = self.shopItems[itemType][foundItem]

                    self.items[itemType].append(foundItem)
                    time.sleep(1)
                    print(f"You have bought {foundItem} for {itemCost} gold!")

                    
                    for stat,value in self.shopItems[itemType][foundItem]["stats"].items():
                        if stat != "cost":
                            setattr(self, stat, getattr(self, stat) + value)
                    #Remove the item from the shop once the player has bought it
                    del self.shopItems[itemType][foundItem]
                    
                    #Ask the user if they want to buy another item
                    buyMore = input("Would you like to buy another item? (y/n): ").lower()
                    #If the user does not want to buy another item they exit the shop
                    if buyMore != 'y':
                        break
                else:
                    print("You don't have enough gold!")
            else:
                print("Invalid item name. Please type the exact name of the item!")
            #Setting the shop as visited after the player exits the shop
            self.shopVisited = True
    #Creating the function for viewing the players inventory
    def viewInventory(self):
        #Display the players inventory until the player decides to go back to the menu
        while True:
            print("\nYour Inventory: ")
            #Display gold in the players inventory
            print("Gold:", self.gold)
            #Display the tools in the players inventory
            print("\nTools:")
            if self.items["Tools"]:
                for item in self.items["Tools"]:
                    itemStats = ", ".join(f"{stat}: {value}" for stat, value in self.inventoryDetails["Tools"][item]["stats"].items())
                    print(f"- {item} ({itemStats})")
            else:
                print("You do not have any Tools")
            #Display the Utility items in the players inventory
            print("\nUtility Items:")
            if self.items["Utility"]:
                for item in self.items["Utility"]:
                    itemStats = ", ".join(f"{stat}: {value}" for stat, value in self.inventoryDetails["Utility"][item]["stats"].items())
                    print(f"- {item} ({itemStats})")
            else:
                print("You do not have any Utility items.")
            #Asking the user if they want to go back to the menu
            goToMenu = input("\nWould you like to go back to the menu? (y/n): ").strip().lower()
            if goToMenu in {'y', 'yes'}:
                break
            elif goToMenu in {'n', 'no'}:
                continue
            
        
    def viewStats(self):
        #Display the players stats until the player decides to go back to the menu
        while True:
            print("\nYour Stats:")
            print(f"Name: {self.name}")
            print(f"Health: {self.health}")
            print(f"Stealth: {self.stealth}")
            print(f"Luck: {self.luck}")
            print(f"Speed: {self.speed}")
            print(f"Quests Completed: {self.questsCompletedCount}")
            #Asking the player if they want to go back to the menu
            goToMenu = input("\nWould you like to go back to the menu? (y/n): ").strip().lower()
            if goToMenu in {'y', 'yes'}:
                break
            elif goToMenu in {'n', 'no'}:
                print("Continuing to display stats...")
                continue
            else:
                print("Invalid input. Please enter 'y', 'yes', 'n', or 'no'.")

    def startNextQuest(self):
        if self.questsCompletedCount == 0:
            print("You have not completed any quests yet!")
            #if no quests are completed the player is then able to start the first quest
            self.stealFromPasserby() #starting the first quest
            
        elif self.challenges: #checking if there are still challenges remaining
            challenge = self.challenges[0] # getting the next challenge
            challengeName = challenge["name"]
            print(f"\nStarting quest: {challengeName}")
                        
            #Adding the logic for the next quests
            if challengeName == "Museum Robbery":
                self.stealFromMuseum()
            elif challengeName == "Royal Relic Robbery":
                self.royalRelicRobbery()
            elif challengeName == "Steal The Kings Crown":
                self.stealKingsCrown()
                
            
            #Update questsCompleteCount and resetting the value of shopVisited after completing a quest
            self.questsCompletedCount += 1
            self.shopVisited = False
            
        else:
            print("You have completed all the quests!, You are the new king!")