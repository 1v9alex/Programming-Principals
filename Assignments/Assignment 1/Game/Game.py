'''
PROG10004 - Programming Principles, Assignment 1
Due Date: Oct 2, 2023
Author: Alexander Gasee
Student Number: 991728593
Professor: Muhammad Asif
'''




from Soldier import Soldier

class Game:
    def __init__(self):
        self.player = None
    
    
    def startGame(self):
        print("Welcome to ????")
        self.chooseRole()
        while True:
            self.displayMenu()
            choice = input("Enter Your Choice: ").lower()
            self.choicePicked(choice)
    
    def chooseRole(self):
        while True:
            roleChoice = input("Choose your role: 1) Soldier or 2) Pickpocket? ").lower()
            if roleChoice == 'soldier':
                playerName = input("Enter your name:")
                self.player = Soldier(playerName,self)
                break
            elif roleChoice == 'pickpocket':
                # implement after soldier is done
                pass
            else:
                print("Invalid choice!")
                
                
    def displayMenu(self):
        print("\nOptions: ")
        print("1) Start Next Quest")
        print("2) Visit Shop")
        print("3) View Inventory")
        print("4) View Stats")
        print("5) Quit Game")
        
    
    def choicePicked(self, choice):
        if choice == '1':
            self.player.startNextQuest()
        elif choice == '2':
            self.player.visitShop()
        elif choice == '3':
            self.player.viewInventory()
        elif choice == '4':
            self.player.viewStats()
        elif choice == '5':
            print("Thanks for playing! Exiting game")
            exit()
        else:
            print("Invalid choice! Please enter a number between 1 and 5")