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
                "Lockpicking Kit": {"cost": 50, "stats": {"stealth": 2, "luck": 1}}, "Extendo Arm": {"cost": 200, "stats":{"stealth": 12,"luck": 5, "speed": 5}},
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

        
            
            
            
            
            
    #Creating the function for the second quest
    def stealFromMuseum(self):
        time.sleep(1)
        print("\nYou find yourself in front of the Royal Museum, known for its precious artifacts stolen from other kingdoms.")
        #Dictionary of artifacts that the pickpocket can steal from along with the difficulty and value
        artifacts = {
            "The Dark Knights Shield": {"difficulty": 6, "value": 100},
            "The Holy Grail": {"difficulty": 10, "value": 300},
            "The Crown Jewels": {"difficulty": 8, "value": 200},
            "The Prophecy": {"difficulty": 15, "value": 500},
            "The Golden Chalice": {"difficulty": 12, "value": 400},
            "The Saviours Pendant": {"difficulty": 20, "value": 1000},
        }
        
        #Rolling  dice to determine the players escape change
        numRolled = random.randint(1, 6) + random.randint(1, 6)
        
        #Displaying the artifacts that the player can steal
        time.sleep(1)
        print("The artifacts you can attempt to steal are:")
        for i, (name, info) in enumerate(artifacts.items(), 1):
            time.sleep(1)
            print(f"{i}. {name} - Value: {info['value']} gold")
        #Loop to continusly ask the player which artifact they want to steal
        while True:
            time.sleep(1)
            choice = input("Which artifact will you attempt to steal? (Enter a number 1-6 or 'exit' to exit) ")
            #Allowing the player to exit the choice loop and end the game
            if choice.lower() == 'exit':
                time.sleep(1)
                print("You decide to leave the museum...")
                time.sleep(1)
                print("Maybe you will come back later")
                time.sleep(1)
                exit()
            #Checking if the players input is valid
            if not (choice.isdigit() and 1 <= int(choice) <= len(artifacts)):
                print("Invalid choice!")
                continue
            
            #Get the chosen artifact details
            artifactName = list(artifacts.keys())[int(choice) - 1]
            artifact = artifacts[artifactName]
            time.sleep(1)
            #Displaying the players choice
            print(f"You attempt to steal {artifactName}")
            time.sleep(1)
            
            #Loop to ask the player how they want to approach the robbery
            while True:
                #Modifying the difficulty based on the players choice
                escapeDifficulty = artifact["difficulty"] - (self.speed // 10)
                
                #Displaying all the different approaches the player can take for the robbery
                time.sleep(1)
                print("\nHow would you like to approach this?")
                time.sleep(1)
                print("1. Try to grab the artifact quickly and escape")
                time.sleep(1)
                print("2. Use your tools and try to disable the security system and take the artifact")
                time.sleep(1)
                print("3. Try to distract the guards and then steal the artifact")
                time.sleep(1)
                
                approachChoice = input("Enter your choice (1-3): ")
                time.sleep(1)
                
                #Adjust the escape difficulty based on the players choice
                if approachChoice == '1':
                    escapeDifficulty -= self.stealth // 10
                    time.sleep(1)
                    print("You try to grab the artifact quickly and escape...")
                elif approachChoice == '2':
                    escapeDifficulty += 1
                    time.sleep(1)
                    print("You attempt to disable the security systems...")
                elif approachChoice == '3':
                    escapeDifficulty -= 1
                    time.sleep(1)
                    print("You try to distract the guards...")
                else:
                    print("Invalid choice!")
                    continue
                
                time.sleep(1)
                
                #Checking if the players roll is less than or equal to the escape difficulty
                if numRolled <= escapeDifficulty:
                    time.sleep(1)
                    #Handling the case where the player fails to steal the artifact
                    print("You were Caught! The Guards Caught you")
                    time.sleep(1)
                    print("You were thrown into the dungeon")
                    time.sleep(1)
                    retry = input("Your heart is racing! Will you try again? (yes/no): ").lower()
                    if retry != 'yes':
                        time.sleep(1)
                        print("You decide it’s time to give up on crime")
                        exit()
                else:
                    #Handling the case where the player successfully steals the artifact
                    print(f"Success! You stole {artifactName} and escaped the museum undetected!")
                    time.sleep(1)
                    print(f"You quickly sell the artifact for {artifact['value']} gold!")
                    self.gold += artifact["value"]
                    time.sleep(1)
                    print(f"You gained {artifact['value']} gold!")
                    self.luck += 2
                    self.stealth += 1
                    self.speed += 4
                    self.challenges.remove({"name": "Museum Robbery", "attribute": "speed"})
                    self.questCompleted = True
                    self.shopVisited = False
                    self.questsCompletedCount += 1
                    return True
                
        
    #Creating the function for the third challenge
    def royalRelicRobbery(self):
        time.sleep(1)
        #Quest/challenge introduction
        print("\nYou find yourself inside the King's Castle, with your eyes set on the Queen's Golden Scepter")
        time.sleep(1)
        #Setting the initial difficulty based on the players stealth stat
        difficulty = 20 - (self.stealth // 10)
        
        #Main quest challenge loop
        while True:
            time.sleep(1)
            print("\nYou're exploring the castle through the secret passageways, trying to find the Queen's room...")
            time.sleep(1)
            
            #Giving player different paths to choose
            print("You come across a three way divide in the passageway, which path will you take?")
            time.sleep(1)
            print("1. The left path which is dimly lit")
            time.sleep(1)
            print("2. The middle path which is brightly lit")
            time.sleep(1)
            print("3. The right path which is pitch black")
            time.sleep(1)
            pathChoice = input("Enter your choice (1-3): ")
            time.sleep(1)
            #Scenario for the left path
            if pathChoice == '1':
                time.sleep(1)
                print("You take the left path")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("You hear a sound, someone is coming. There is a door to your right, what will you do?")
                time.sleep(1)
                print("1. Hide in the room")
                time.sleep(1)
                print("2. Continue Walking and attempt to fool the person")
                time.sleep(1)
                actionChoice = input("Enter your choice (1-2): ")
                #Based on the action modify the difficulty or stats (or both) of the player and mission
                if actionChoice == '1':
                    time.sleep(1)
                    print("You hide in the room. It was just the royal maid who was passing by without entering the room")
                    difficulty -= 1
                elif actionChoice == '2':
                    time.sleep(1)
                    print("You continue walking The person walking was just a cook he didn't notice you")
                    self.stealth += 2
                else:
                    print("Invalid choice!")
                    continue
                #Scenario for the middle path
            elif pathChoice == '2':
                time.sleep(1)
                print("You take the brightly lit middle path")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("You hear guards in the distance this is going to be risky")
                time.sleep(1)
                difficulty += 4
                time.sleep(1)
                print("You see a guard approaching you, what will you do?")
                time.sleep(1)
                print("1. Hide under some furniture")
                time.sleep(1)
                print("2. Try to quietly knock him out")
                time.sleep(1)
                actionChoice = input("Enter your choice (1-2): ")
                if actionChoice == '1':
                    time.sleep(1)
                    print("You hide under a table, the guard didn't notice you")
                    difficulty -= 2
                    self.stealth += 2
                elif actionChoice == '2':
                    time.sleep(1)
                    print("You try to knock him out, but he notices you and calls for backup")
                    time.sleep(1)
                    print("You are caught and thrown into the dungeon")
                    time.sleep(1)
                    retry = input("Challenge Failed! Will you try again? (yes/no): ").lower()
                    if retry != 'yes':
                        time.sleep(1)
                        print("You decide it’s time to give up on crime")
                        exit()
                else:
                    print("Invalid choice!")
                    continue
                #Scenario for the right path
            elif pathChoice == '3':
                time.sleep(1)
                print("You take the pitch black right path, its safer but who knows whats in there")
                difficulty -= 2
                time.sleep(1)
                print("You trip on something, it's a sleeping guard dog, what will you do?")
                time.sleep(1)
                print("1. Try to sneak past it")
                time.sleep(1)
                print("2. Distract it with a piece of meat")
                time.sleep(1)
                actionChoice = input("Enter your choice (1-2): ")
                if actionChoice == '1':
                    time.sleep(1)
                    print("You sneak past the dog, it didnt wave up. You continue walking")
                    self.stealth += 2
                    self.luck += 1
                elif actionChoice == '2':
                    time.sleep(1)
                    print("You distract the dog with a piece of meat, it eats the meat and you continue walking")
                    self.luck += 2
                    self.stealth += 1
                else:
                    print("Invalid choice!")
                    continue
            #Rolling the dice to determine the players success
            numRolled = random.randint(1, 6) + random.randint(1, 6)
            escapeDifficulty = difficulty - (self.speed // 10)
            #Comparing the roll to the escape difficulty to see if the player was successful
            if numRolled >= escapeDifficulty:
                #Handling the case where the player successfully steals the Queens Scepter
                time.sleep(1)
                print("You found the Queen's room, you manages to secure the Queen's Golden Scepter!")
                self.challenges.remove({"name": "Royal Relic Robbery", "attribute": "stealth"})
                self.questCompleted = True
                self.shopVisited = False
                self.questsCompletedCount += 1
                self.luck += 2
                self.stealth += 2
                self.speed += 2
                time.sleep(1)
                #Giving the player the option to leave the kingdom or to stay and try to steal the Kings Crown
                print("You realise now that you've stolen the Queens Scepter you will have to leave the kingdom")
                time.sleep(1)
                print("Will you decide to leave the kingdom and start a new life? or will you stay and try to steal the Kings Crown?")
                time.sleep(1)
                actionChoice = input("Enter your choice (1-2): ")
                if actionChoice == '1':
                    time.sleep(1)
                    print("You decide to leave the kingdom and start a new life")
                    time.sleep(1)
                    print("You have completed all the quests!, You started a new life in the rival kingdom and bought your way to power! You are the new king!")
                    time.sleep(2)
                    exit()
                elif actionChoice == '2':
                    time.sleep(1)
                    print("You decide to stay and try to steal the Kings Crown")
                    self.stealKingsCrown()
                return True
            else:
                #Handling the case where the player fails to steal the Queens Scepter
                time.sleep(1)
                print("You were Caught! The Guards Caught you and threw you into the dungeon where you will wait to be executed!")
                time.sleep(1)
                retry = input("Challenge Failed! Will you try again? (yes/no): ").lower()
                if retry != 'yes':
                    time.sleep(1)
                    print("You decide it’s time to give up on crime")
                    exit()

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