import random
import string
import time

#Creating and initalizing the soldier class

'''
TODO
Fix prints for the dragon battle to make it read better
Add dragon attacking to make the battle harder
'''
class Soldier:
    def __init__(self, name):
        #Initializing the attributes of the soldier
        self.name = name
        self.gold = 100
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
                "Dragon's Tooth": {"cost": 10, "stats": {"damage": 3, "stamina": 1}}, "Excalibur": {"cost": 100, "stats": {"damage":15,"health":10}},
                "Blade Of Steel": {"cost": 5, "stats": {"damage": 2}}, "Holy Sword": {"cost": 100, "stats": {"damage": 10, "health": 10, "armour": 5,"stamina": 2}},
                "Blade Of The Fallen": {"cost": 50, "stats":{"damage": 5,"health": 5, "armour": 3}}, "Long Sword": {"cost": 30, "stats": {"damage": 4}},
            },
            "Defensive": {
                "Armour Of The Gods": {"cost": 80, "stats": {"armour": 10, "health": 10, "stamina": 5}}, "Boots Of Quickness": {"cost": 50, "stats": {"stamina": 5}},
                "Iron Armour": {"cost": 20, "stats": {"armour": 5, "health": 5}}, "Shield Of The Gods": {"cost": 100, "stats": {"armour": 10, "health": 10, "stamina": 5}},
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
                            damage = dragonAttack - self.armour
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
        while True:
            choice = ""
            
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

            choice = input("You have two options 1) Sneak in the kingdom and try to kill the king or 2) Call your fellow soldiers to invade the kingdom ")
            time.sleep(2)

            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            numRolled = die1 + die2
            missionComplete = False

            while self.stamina > 0:
                print(f"Your stamina: {self.stamina}")

                if choice == '1':
                    print("You decide to sneak in the kingdom and try to kill the king")
                    time.sleep(1)
                    print("You decide to walk around the kingdom to see if you can find the king")
                    time.sleep(1)
                    print("After a sneaking around for a while you manage to make it into the castle")
                    time.sleep(2)
                    print("The castle is heavily guarded you have to sneak around, if you get caught you will be thrown in the dungeon")
                    time.sleep(1)
                    hiddenCheck = random.randint(2, 12) + self.stamina + numRolled

                    if hiddenCheck >= 10:
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
                        print("You Were Spotted! The kings guards are chasing you, you need to run!")
                        self.stamina -= random.randint(1, 3)
                        if self.stamina <= 0:
                            print("You were caught and thrown in the dungeon! The Assassination failed!")
                            break  # Exiting the inner while loop
                        else:
                            print("You managed to escape and hide. But you lost your stamina running")

                elif choice == '2':
                    print("You decide to call your fellow soldiers to invade the kingdom")
                    battleCheck = random.randint(2, 12) + self.stamina + numRolled

                    if battleCheck >= 10:
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
                        print("The kingdom defenses are strong. You and your soldiers need to retreat!")
                        self.stamina -= random.randint(1, 3)
                        if self.stamina <= 0:
                            print("Your soldiers were defeated and you were captured! The invasion failed!")
                            break  # Exiting the inner while loop
                        else:
                            print("You managed to escape and hide. But you lost your stamina running")

                else:
                    print("Invalid Input. Please Enter '1' or '2'")

            # If mission was not completed and stamina <= 0
            print("You have failed your quest!")
            retry = input("You have failed the mission. Would you like to retry? (yes/no): ").lower()
            if retry != 'yes':
                print("Thanks for playing! Exiting game")
                time.sleep(2)
                exit()
                
    def overthrowKing(self):
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
                choice = input("Are you ready to duel the king? (y/n): ").lower()
                
                if choice in {'n','no'}:
                    print("Retreating wont help you become king! Gather your courage and fight!")
                    continue
                elif choice not in {'y','yes'}:
                    print("Invalid Input. Please Enter 'y', 'yes', 'n', or 'no'")
                    continue
                
                inBattle = True
                
                while self.health > 0 and kingHealth > 0:
                    print(f"Your Health: {self.health}, Your Armour: {self.armour}, King's Health: {kingHealth}, King's Armour: {kingArmour}")
                    
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
                            
                        #King's attack
                        kingAttack = random.randint(2,12)
                        if kingAttack > self.armour:
                            print("The king strikes back and you take damage!")
                            self.health -= (kingAttack - self.armour + kingDamage)
                    
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
                    
                    if kingHealth <= 1:
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
                        print("You have been defeated by the king!")
                        retry = input("Would you like to retry? (yes/no): ").lower()
                        if retry == 'yes':
                            self.health = 50
                            kingHealth = 50
                            kingArmour = 5
                            continue
                        else:
                            print("Thanks for playing! Exiting game")
                            time.sleep(2)
                            exit()
                            
                if inBattle:
                    break
        
        
    
    def becomeKing(self):
        print("\nFinal Mission: Battle against the kings best solider!")
        time.sleep(1)
        print("...")
        print("The Dark Knight has arrived!")
        time.sleep(1)
        
        darkKnightHealth = 50
        darkKnightDamage = 3
        darkKnightArmour = 8
        darkKnightStamina = 8
        

        

        while True:
            print("\nYour Health:", self.health)
            print("Dark Knight's Health:", darkKnightHealth)
            
            actions = ["Attack", "Defend"]
            if self.stamina >= 10:
                actions.append("Special Attack")
            
            print("Available Actions:", ", ".join(actions))
            choice = input("Choose your action: 1) Attack or 2) Defend or 3) Special Attack: ").lower()
            
            
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            numRolled = die1+die2
            darkKnightAttack = darkKnightDamage + numRolled
                        
            if choice == '1': #Attack Logic
                if numRolled + self.stamina > darkKnightArmour:
                    print("You pierce through the Dark Knight's armour and deal damage!")
                    damageDealt = numRolled + self.damage - darkKnightArmour
                    darkKnightHealth -= max(damageDealt, 0)
                    darkKnightArmour = max(darkKnightArmour - 1, 0)
                else:
                    print("The Dark Knight's armour is too strong, he blocked your attack!")
                
                #Dark Knight's attack
                if darkKnightAttack > self.armour:
                    print("The Dark Knight strikes back and you take damage!")
                    self.health -= max(darkKnightAttack - self.armour + darkKnightDamage, 0)
                    
            elif choice == '2': #Defend logic
                print("You decide to defend against the Dark Knight's attack!")
                darkKnightAttack = random.randint(2,12)
                if darkKnightAttack > self.armour:
                    print("The Dark Knight pierces through your defense!")
                    reducedDamage = max(darkKnightAttack - self.armour - numRolled,0)
                    self.health -= reducedDamage
                else:
                    print("You successfully defended against the Dark Knight's attack!")
            
            elif choice == '3' and "Special Attack" in actions:
                print("You used your most powerful attack!")
                if self.stamina >= 10:
                    #Charge attack if high stamina
                    print("You charge at the Dark Knight with immense power!")
                    darkKnightHealth -= self.damage + 1 + numRolled
                
                elif self.armour >= 10:
                    #High armour you will do a shield attack
                    print("You use your shield to attack the Dark Knight lowering his armour!")
                    darkKnightArmour = max(darkKnightArmour - numRolled, 0)
                else:
                    print("Your special move fails!")
                    
            #Dark knights turn
            if darkKnightHealth > 0:
                if self.damage >= 10:
                    print("The Dark knight focuses on defending and countering!")
                    
                    #Counter/Parry Logic
                    counterAttack = random.randint(2,12)
                    if counterAttack > self.armour:
                        print("The Dark Knight counters your attack!")
                        self.health -= max(counterAttack - self.armour + darkKnightDamage, 0)
                    else:
                        print("You successfully defended against the Dark Knight's counter attack!")
                else:
                    print("The Dark Knight attacks!")
                    
                    #Dark Knight's attack LOGIC
                    darkKnightAttack = random.randint(2,12)
                    if darkKnightAttack > self.armour:
                        print("The Dark Knight strikes back and you take damage!")
                        self.health -= max(darkKnightAttack - self.armour + darkKnightDamage, 0)
                    else:
                        print("You successfully defended against the Dark Knight's attack!")
            # Check win/lose conditions
            if darkKnightHealth <= 0:
                print("You have defeated the Dark Knight!")
                print("Congratulations! You now rule the kingdom!")
                
                # Ask the player if they want to restart the game or exit
                restart = input("Would you like to restart the game and choose a different role? (yes/no): ").lower()
                if restart == 'yes':
                    print("CODE LOGIC FOR RESTARTING GAME")
                    # Restart the game
                    #TODO CODE LOGIC FOR STARTING GAME
                else:
                    print("Thanks for playing! Exiting game")
                    exit()
                    
            elif self.health <= 0:
                print("You have been defeated by the Dark Knight!")
                
                # Ask the player if they want to retry or exit
                retry = input("Would you like to retry? (yes/no): ").lower()
                if retry == 'yes':
                    # Reset player and Dark Knight's health and continue the battle
                    self.health = 50  # or any other logic to restore player's health
                    darkKnightHealth = 50
                    continue
                else:
                    print("Thanks for playing! Exiting game")
                    exit()
                            
            
            
            
            
        
    def visitShop(self):
        #Creating the logic for visiting the shop
        if self.questsCompletedCount <= 0 or (self.questsCompletedCount <= len(self.challenges) and self.shopVisited):
            print("You cant visit the shop now!")
            return
        
        
        while True:
            #Loop to print the shop items
            print("\nWelcome to the shop!")
            print("You Currently Have:", self.gold, "gold")
            time.sleep(2)
                
            print("Offensive Items:")
            for itemName, itemDetails in self.shopItems["Offensive"].items():
                print(f"{itemName}: {itemDetails['cost']} gold")
                
            print("\nDefensive Items:")
            for itemName, itemDetails in self.shopItems["Defensive"].items():
                print(f"{itemName}: {itemDetails['cost']} gold")
                
            itemToBuy = input("\nWhat would you like to buy? (Type 'exit' to exit): ").title()
            formattedInput = itemToBuy.strip().lower().translate(str.maketrans('', '', string.punctuation))
            
            if formattedInput == 'exit':
                break
            
            foundItem = None
            itemType = None
            
            #Checking if the item exists in the shop
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
                itemCost = self.shopItems[itemType][foundItem]["cost"]
                if self.gold >= itemCost:
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
                    
                    buyMore = input("Would you like to buy another item? (y/n): ").lower()
                    if buyMore != 'y':
                        break
                else:
                    print("You don't have enough gold!")
            else:
                print("Invalid item name. Please type the exact name of the item!")
                
            self.shopVisited = True
            

            
            
    
    def viewInventory(self):
        #Creating the logic for viewing the inventory
        while True:
            print("\nYour Inventory: ")
            print("Gold:", self.gold)
            print("\nOffensive Items:")
            if self.items["Offensive"]:
                for item in self.items["Offensive"]:
                    itemStats = ", ".join(f"{stat}: {value}" for stat, value in self.inventoryDetails["Offensive"][item]["stats"].items())
                    print(f"- {item} ({itemStats})")
            else:
                print("You do not have any offensive items.")
                
            print("\nDefensive Items:")
            if self.items["Defensive"]:
                for item in self.items["Defensive"]:
                    itemStats = ", ".join(f"{stat}: {value}" for stat, value in self.inventoryDetails["Defensive"][item]["stats"].items())
                    print(f"- {item} ({itemStats})")
            else:
                print("You do not have any defensive items.")
                
            goToMenu = input("\nWould you like to go back to the menu? (y/n): ").strip().lower()
            if goToMenu in {'y', 'yes'}:
                break
            elif goToMenu in {'n', 'no'}:
                continue
            
        
    def viewStats(self):
        #Creating the logic for viewing the players stats
        print("\nYour Stats:")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Armour: {self.armour}")
        print(f"Stamina: {self.stamina}")
        print(f"Quests Completed: {self.questsCompletedCount}")
        

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
                
            
            #Update questsCompleteCount and reseting the value of shopVisited after completing a quest
            self.questsCompletedCount += 1
            self.shopVisited = False
            
        else:
            print("You have completed all the quests!, You are the new king!")
            