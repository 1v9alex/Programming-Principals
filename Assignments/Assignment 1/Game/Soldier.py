import random
import string
import time
#Creating and initalizing the soldier class
class Soldier:
    def __init__(self, name,game):
        #Initializing the attributes of the soldier
        self.name = name
        self.game = game
        self.gold = 10
        self.health = 50
        self.damage = 2
        self.armour = 1
        self.stamina = 2
        self.questCompleted = False
        self.shopVisited = True
        self.questsCompletedCount = 0
        #Dictionary of items that the soldier has
        self.items = {"Offensive": [], "Defensive": []}
        self.inventoryDetails = {"Offensive": {}, "Defensive": {}}
        #List of challenges that the soldier has to complete
        self.challenges = [
            {"name": "Battle your first dragon", "attribute": "damage"},
            {"name": "Invade your first kingdom", "attribute": "stamina"},
            {"name": "Overthrow the evil king", "attribute": "armour"},
            {"name": "Become The King", "attribute": "Damage"}
                        
                        ]
        #Dictionary of items that the shop has for the soldier role
        self.shopItems = {
            "Offensive": {
                "Developer Item" : {"cost": 10000,"stats": {"damage": 100000,"stamina": 100000, "armour": 1000000,"health": 1000000}},
                "Dragon's Tooth": {"cost": 10, "stats": {"damage": 3, "stamina": 1}}, "Excalibur": {"cost": 100, "stats": {"damage":15,"health":10}},
                "Blade Of Steel": {"cost": 5, "stats": {"damage": 2}}, "Holy Sword": {"cost": 100, "stats": {"damage": 10, "health": 10, "armour": 5,"stamina": 2}},
                "Blade Of The Fallen": {"cost": 50, "stats":{"damage": 5,"health": 5, "armour": 3}}, "Long Sword": {"cost": 30, "stats": {"damage": 4}},
            },
            "Defensive": {
                "Armour Of The Gods": {"cost": 80, "stats": {"armour": 10, "health": 10, "stamina": 5}}, "Boots Of Quickness": {"cost": 50, "stats": {"stamina": 5}},
                "Iron Armour": {"cost": 20, "stats": {"armour": 5, "health": 5}}, "Shield Of The Gods": {"cost": 100, "stats": {"armour": 10, "health": 10, "stamina": 5}},
            }
        }
        
        #function for the battle dragon challenge
    def battleDragon(self):
        #Printing the intro to the first quest
        print("\nFirst Challenge: Battle your first dragon!")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("A dragon appears before you!")
        
        #Initializing dragons stats
        dragonHealth = 30
        dragonDamage = 3
        
        #Starting the battle loop
        while True:
            #Displaying both the players health and the dragons health
            print("\nYour Health:", self.health)
            print("Dragon's Health:", dragonHealth)
            
            #Array for the actions that the player can take
            actions = ["Attack", "Defend"]
            
            print("Available Actions:", ", ".join(actions))
            choice = input("Choose your action: 1) Attack or 2) Defend: ").lower()
            time.sleep(1)
            
            #Rolling the dice for outcomes
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            numRolled = die1 + die2
            dragonAttack = dragonDamage + numRolled
            
            #Creating the logic for the players actions
            #If the player chooses to attack we determine the outcome of the attack
            if choice == '1' or choice == 'attack':
                print(f"You decide to attack the dragon!, you rolled a {numRolled}")
                damageDealt = numRolled + self.damage
                dragonHealth -= max(damageDealt, 0)
                
                if dragonHealth > 0:
                    time.sleep(1)
                    print("The dragon retaliates!")
                    self.health -= max(dragonAttack - self.armour, 0)
                    #If the player chooses to attack we determine the outcome of the attack
            elif choice == '2' or choice == 'defend':
                print("You decide to defend against the dragon!")
                if dragonAttack > self.armour:
                    time.sleep(1)
                    print("The dragon's fire breath is too strong!")
                    reducedDamage = max(dragonAttack - self.armour, 0)
                    self.health -= reducedDamage
                else:
                    time.sleep(1)
                    print("You successfully defended against the dragon's attack!")
            
            # Check win/lose conditions
            if dragonHealth <= 0:
                time.sleep(1)
                #If the player wins the battle we remove the challenge from the list and give the player rewards
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
                #If the player loses the battle we ask them if they want to retry or exit the game
                time.sleep(1)
                print("You have been defeated by the dragon!")
                retry = input("Would you like to retry? (yes/no): ").lower()
                if retry == 'yes':
                    self.health = 50
                    dragonHealth = 30
                    continue
                else:
                    time.sleep(1)
                    print("Thanks for playing! Exiting game")
                    exit()

                
    #Define the function for the invade kingdom challenge
    def invadeKingdom(self):
        #Printing the intro to the second quest
        while True:
            #Restting the choice variable
            choice = ""
            
            #Resetting the players stamina
            self.stamina = 2

            print("A fellow solider noticed your fight against that dragon and has tasked you with scouting a nearby kingdom to see if it is weak enough to invade")
            time.sleep(1)
            print("You arrive at the kingdom and notice that it is heavily guarded")
            time.sleep(1)
            print("You decide to sneak into the kingdom to see if you can find any weaknesses")
            time.sleep(1)
            print("You find a weak spot in the wall and decide to sneak in")
            time.sleep(1)
            print("Your goal is to not get caught inside the kingdom")
            time.sleep(1)
            
            #Getting the players choice for the mission
            choice = input("You have two options 1) Sneak in the kingdom and try to kill the king or 2) Call your fellow soldiers to invade the kingdom ")
            time.sleep(2)
            
            #roll the dice to determine the outcome later on
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            numRolled = die1 + die2
            missionComplete = False
            
            #Starting the mission loop
            while self.stamina > 0:
                #Displaying the players stamina
                print(f"Your stamina: {self.stamina}")

                if choice == '1':
                    #Creating the logic for the players choice, because they chose 1 they will try to sneak in the kingdom and kill the king
                    print("You decide to sneak in the kingdom and try to kill the king")
                    time.sleep(1)
                    print("You decide to walk around the kingdom to see if you can find the king")
                    time.sleep(1)
                    print("After a sneaking around for a while you manage to make it into the castle")
                    time.sleep(2)
                    print("The castle is heavily guarded you have to sneak around, if you get caught you will be thrown in the dungeon")
                    time.sleep(1)
                    hiddenCheck = random.randint(2, 12) + self.stamina + numRolled
                    
                    #Checking if the player was caught or not
                    if hiddenCheck >= 10:
                        #Since the player completed the challenge they are rewarded
                        print("You managed to successfully sneak through the kingdom and assassinate the king, you are now the king!")
                        missionComplete = True
                        self.gold += 100
                        self.stamina += 2
                        self.damage += 1
                        self.armour += 2
                        self.challenges.remove({"name": "Invade your first kingdom", "attribute": "stamina"})
                        self.questCompleted = True
                        self.shopVisited = False
                        self.questsCompletedCount += 1
                        return True
                    else:
                        #If the player was caught they will lose stamina and if their stamina reaches 0 they will fail the mission
                        time.sleep(1)
                        print("You Were Spotted! The kings guards are chasing you, you need to run!")
                        time.sleep(1)
                        self.stamina -= random.randint(1, 3)
                        if self.stamina <= 0:
                            print("You were caught and thrown in the dungeon! The Assassination failed!")
                            time.sleep(1)
                            break  # Exiting the inner while loop
                        else:
                            print("You managed to escape and hide. But you lost your stamina running")
                elif choice == '2':
                    #Creating the logic for the players choice, because they chose 2 they will call their fellow soldiers to invade the kingdom
                    print("You decide to call your fellow soldiers to invade the kingdom")
                    battleCheck = random.randint(2, 12) + self.stamina + numRolled

                    if battleCheck >= 10:
                        #Since the player completed the challenge they are rewarded
                        print("You fought a hard battle, you and your soldiers manage to take over the kingdom! Victory is yours.")
                        missionComplete = True
                        self.gold += 60
                        self.stamina += 2
                        self.damage += 1
                        self.armour += 2
                        self.challenges.remove({"name": "Invade your first kingdom", "attribute": "stamina"})
                        self.questCompleted = True
                        self.shopVisited = False
                        self.questsCompletedCount += 1
                        return True
                    else:
                        #If the player was caught they will lose stamina and if their stamina reaches 0 they will fail the mission
                        time.sleep(1)
                        print("The kingdom defenses are strong. You and your soldiers need to retreat!")
                        self.stamina -= random.randint(1, 3)
                        if self.stamina <= 0:
                            time.sleep(1)
                            print("Your soldiers were defeated and you were captured! The invasion failed!")
                            break  # Exiting the inner while loop
                        else:
                            time.sleep(1)
                            print("You managed to escape and hide. But you lost your stamina running")

                else:
                    #If the player enters an invalid input they will be asked to enter a valid input
                    print("Invalid Input. Please Enter '1' or '2'")

            # If mission was not completed and stamina <= 0
            print("You have failed your quest!")
            retry = input("You have failed the mission. Would you like to retry? (yes/no): ").lower()
            if retry != 'yes':
                print("Thanks for playing! Exiting game")
                time.sleep(2)
                exit()
    #Define the function for the overthrow king challenge
    def overthrowKing(self):
        #Printing the intro to the third quest
        print("Now that you have your own kingdom, its time to overthrow the evil king from your old kingdom!")
        time.sleep(2)
        print("Your old kingdom has a much stronger army then you so you have to go alone.")
        time.sleep(2)
        print("You find the king and challenge him to a duel to the death, and he accepts!")
        time.sleep(2)
        
        #Setting up variables for the kings stats
        kingHealth = 50
        kingDamage = 5
        kingArmour = 2
        inBattle = False
        
        while True: #Creating a loop that will run until you choose to battle the king
            if not inBattle:
                #Asking the user if they are ready to battle the king
                choice = input("Are you ready to duel the king? (y/n): ").lower()
                
                if choice in {'n','no'}:
                    print("Retreating wont help you become king! Gather your courage and fight!")
                    continue
                elif choice not in {'y','yes'}:
                    print("Invalid Input. Please Enter 'y', 'yes', 'n', or 'no'")
                    continue
                #The battle loop this is where the battle begins
                inBattle = True
                
                while self.health > 0 and kingHealth > 0:
                    #A print statement to display the current stats of the king and the player
                    print(f"Your Health: {self.health}, Your Armour: {self.armour}, King's Health: {kingHealth}, King's Armour: {kingArmour}")
                    
                    #Asking the player which action they would like to do
                    choice = input("Do you want to 1) Attack or 2) Defend")
                    die1 = random.randint(1,6)
                    die2 = random.randint(1,6)
                    numRolled = die1 + die2
                    print(f"You rolled a {numRolled}")
                    
                    if choice == '1': #Attack logic
                        if numRolled > kingArmour:
                            print("You pierce through the king's armour and deal damage!")
                            kingHealth -= (numRolled - kingArmour + self.damage)
                            kingArmour = max(kingArmour - 1, 0)
                        else:
                            print("The king's armour is too strong he blocked your attack!")
                            
                        #King's attack logic
                        kingAttack = random.randint(2,12)
                        if kingAttack > self.armour:
                            print("The king strikes back and you take damage!")
                            self.health -= (kingAttack - self.armour + kingDamage)
                    #Defend logic
                    elif choice == '2':
                        print("You decide to defend against the king's attack!")
                        kingAttack = random.randint(2,12)
                        if kingAttack > self.armour:
                            print("The king pierces through your defense!")
                            reducedDamage = max(kingAttack - self.armour - numRolled,0) #Damage is reduced by the amount rolled on the dice
                            self.health -= reducedDamage
                        else:
                            print("You successfully defended against the king's attack!")
                    else:
                        print("Invalid Input. Please Enter '1' or '2'")
                        continue
                    #Checking the win/loss condition
                    if kingHealth <= 0:
                        #if the player wins the battle they are rewarded
                        print("You have defeated the king!")
                        time.sleep(1)
                        print("Its almost time to take the throne!")
                        self.challenges.remove({"name": "Overthrow the evil king", "attribute": "armour"})
                        self.gold += 100
                        self.armour += 2
                        self.damage += 2
                        self.stamina += 2
                        self.questCompleted = True
                        self.shopVisited = False
                        self.questsCompletedCount += 1
                        break
                    elif self.health <= 0:
                        #If the player loses the battle they will be asked if they want to retry or exit the game
                        print("You have been defeated by the king!")
                        retry = input("Would you like to retry? (yes/no): ").lower()
                        if retry == 'yes':
                            self.health = 50
                            kingHealth = 50
                            kingArmour = 5
                            continue
                        else:
                            #If the player chooses to exit the game the game will exit
                            print("Thanks for playing! Exiting game")
                            time.sleep(2)
                            exit()
                            
                if inBattle:
                    break
        
    '''Define the function for the become king challenge
    This is the final challenge of the game, 
    if the player wins this battle they will become the king
    '''
    def becomeKing(self):
        #Prints the intro to the final quest
        print("\nFinal Mission: Battle against the kings best solider!")
        time.sleep(1)
        print("...")
        print("The Dark Knight has arrived!")
        time.sleep(1)
        #Setting up the dark knights stats
        darkKnightHealth = 50
        darkKnightDamage = 3
        darkKnightArmour = 8
        darkKnightStamina = 8
        
        while True:
            #Displaying the players health and the dark knights health
            print("\nYour Health:", self.health)
            print("Dark Knight's Health:", darkKnightHealth)
            
            #Determine available actions based on the players stats
            actions = ["Attack", "Defend"]
            #If the players stamina is >= 10 they can use their special attack
            if self.stamina >= 10:
                #Adding "Special Attack" to the actions list if the player meets the criteria
                actions.append("Special Attack")
            #Printing the available actions
            print("Available Actions:", ", ".join(actions))
            #Players turn to choose an action
            choice = input("Choose your action: 1) Attack or 2) Defend or 3) Special Attack: ").lower()
            time.sleep(1)
            
            #Rolling the dice for outcomes
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            numRolled = die1+die2
            darkKnightAttack = darkKnightDamage + numRolled
                        
            if choice == '1': #Attack Logic
                if numRolled + self.stamina > darkKnightArmour:
                    time.sleep(1)
                    print("You pierce through the Dark Knight's armour and deal damage!")
                    damageDealt = numRolled + self.damage - darkKnightArmour
                    darkKnightHealth -= max(damageDealt, 0)
                    darkKnightArmour = max(darkKnightArmour - 1, 0)
                else:
                    time.sleep(1)
                    print("The Dark Knight's armour is too strong, he blocked your attack!")
                
                #Dark Knight's attack logic
                if darkKnightAttack > self.armour:
                    time.sleep(1)
                    print("The Dark Knight strikes back and you take damage!")
                    self.health -= max(darkKnightAttack - self.armour + darkKnightDamage, 0)
                    
            elif choice == '2': #Defend logic
                time.sleep(1)
                print("You decide to defend against the Dark Knight's attack!")
                darkKnightAttack = random.randint(2,12)
                if darkKnightAttack > self.armour:
                    time.sleep(1)
                    print("The Dark Knight pierces through your defense!")
                    reducedDamage = max(darkKnightAttack - self.armour - numRolled,0)
                    self.health -= reducedDamage
                else:
                    time.sleep(1)
                    print("You successfully defended against the Dark Knight's attack!")
            #Special attack logic, for the different types of special attacks
            elif choice == '3' and "Special Attack" in actions:
                time.sleep(1)
                print("You used your most powerful attack!")
                if self.stamina >= 10:
                    #Charge attack if high stamina
                    time.sleep(1)
                    print("You charge at the Dark Knight with immense power!")
                    darkKnightHealth -= self.damage + 1 + numRolled
                
                elif self.armour >= 10:
                    #High armour you will do a shield attack
                    time.sleep(1)
                    print("You use your shield to attack the Dark Knight lowering his armour!")
                    darkKnightArmour = max(darkKnightArmour - numRolled, 0)
                else:
                    time.sleep(1)
                    print("Your special move fails!")
                    
            #Dark knights turn
            if darkKnightHealth > 0:
                if self.damage >= 10:
                    time.sleep(1)
                    print("The Dark knight focuses on defending and countering!")
                    
                    #Counter/Parry Logic
                    counterAttack = random.randint(2,12)
                    if counterAttack > self.armour:
                        time.sleep(1)
                        print("The Dark Knight counters your attack!")
                        self.health -= max(counterAttack - self.armour + darkKnightDamage, 0)
                    else:
                        time.sleep(1)
                        print("You successfully defended against the Dark Knight's counter attack!")
                else:
                    time.sleep(1)
                    print("The Dark Knight attacks!")
                    
                    #Dark Knight's attack LOGIC
                    darkKnightAttack = random.randint(2,12)
                    if darkKnightAttack > self.armour:
                        time.sleep(1)
                        print("The Dark Knight strikes back and you take damage!")
                        self.health -= max(darkKnightAttack - self.armour + darkKnightDamage, 0)
                    else:
                        time.sleep(1)
                        print("You successfully defended against the Dark Knight's attack!")
            # Check win/lose conditions
            if darkKnightHealth <= 0:
                time.sleep(1)
                print("You have defeated the Dark Knight!")
                time.sleep(1)
                print("Congratulations! You now rule the kingdom!")
                time.sleep(1)
                # Ask the player if they want to restart the game or exit
                restart = input("Would you like to restart the game and choose a different role? (yes/no): ").lower()
                if restart == 'yes':
                    print("CODE LOGIC FOR RESTARTING GAME")
                    # Restart the game
                    self.game.chooseRole()
                else:
                    time.sleep(1)
                    print("Thanks for playing! Exiting game")
                    time.sleep(1)
                    exit()
                    
            elif self.health <= 0:
                time.sleep(1)
                print("You have been defeated by the Dark Knight!")
                time.sleep(1)
                # Ask the player if they want to retry or exit
                retry = input("Would you like to retry? (yes/no): ").lower()
                if retry == 'yes':
                    # Reset player and Dark Knight's health and continue the battle
                    self.health = 50  # or any other logic to restore player's health
                    darkKnightHealth = 50
                    continue
                else:
                    # Exit the game
                    time.sleep(1)
                    print("Thanks for playing! Exiting game")
                    exit()
                            
            
            
            
            
    #Creating the function for the item shop
    def visitShop(self):
        #Check if the player is able to visit the shop based on quest completion and if they have already visited the shop
        if self.questsCompletedCount <= 0 or (self.questsCompletedCount <= len(self.challenges) and self.shopVisited):
            print("You cant visit the shop now!")
            time.sleep(2)
            return
        
        
        while True:
            #Printing welcome message and the players gold amount
            print("\nWelcome to the shop!")
            print("You Currently Have:", self.gold, "gold")
            time.sleep(2)
            #Display offensive items (attacking focused items) available in the shop
            print("Offensive Items:")
            for itemName, itemDetails in self.shopItems["Offensive"].items():
                print(f"{itemName}: {itemDetails['cost']} gold")
            #Display defensive items (defense/health focused items) available in the shop
            print("\nDefensive Items:")
            for itemName, itemDetails in self.shopItems["Defensive"].items():
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
            #Display the offensive items in the players inventory
            print("\nOffensive Items:")
            if self.items["Offensive"]:
                for item in self.items["Offensive"]:
                    itemStats = ", ".join(f"{stat}: {value}" for stat, value in self.inventoryDetails["Offensive"][item]["stats"].items())
                    print(f"- {item} ({itemStats})")
            else:
                print("You do not have any offensive items.")
            #Display the defensive items in the players inventory
            print("\nDefensive Items:")
            if self.items["Defensive"]:
                for item in self.items["Defensive"]:
                    itemStats = ", ".join(f"{stat}: {value}" for stat, value in self.inventoryDetails["Defensive"][item]["stats"].items())
                    print(f"- {item} ({itemStats})")
            else:
                print("You do not have any defensive items.")
            #Asking the user if they want to go back to the menu
            goToMenu = input("\nWould you like to go back to the menu? (yes/no): ").strip().lower()
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
            print(f"Damage: {self.damage}")
            print(f"Armour: {self.armour}")
            print(f"Stamina: {self.stamina}")
            print(f"Quests Completed: {self.questsCompletedCount}")
            #Asking the player if they want to go back to the menu
            goToMenu = input("\nWould you like to go back to the menu? (yes/no): ").strip().lower()
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
            self.battleDragon() #starting the first quest
            
        elif self.challenges: #checking if there are still challenges remaining
            challenge = self.challenges[0] # getting the next challenge
            challengeName = challenge["name"]
            print(f"\nStarting quest: {challengeName}")
                        
            #Adding the logic for the next quests
            if challengeName == "Invade your first kingdom":
                self.invadeKingdom()
            elif challengeName == "Overthrow the evil king":
                self.overthrowKing()
            elif challengeName == "Become The King":
                self.becomeKing()
                
            
            #Update questsCompleteCount and resetting the value of shopVisited after completing a quest
            self.questsCompletedCount += 1
            self.shopVisited = False
            
        else:
            print("You have completed all the quests!, You are the new king!")
            