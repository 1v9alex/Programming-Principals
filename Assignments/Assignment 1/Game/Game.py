'''
PROG10004 - Programming Principles, Assignment 1
Due Date: Oct 11, 2023
Author: Alexander Gasee
Student Number: 991728593
Professor: Muhammad Asif
'''
import time
from Soldier import Soldier
from Pickpocket import Pickpocket
#Creating a game class to handle the game
class Game:
    def __init__(self):
        '''
        Constructor for the Game class. Initializes the player to None.
        '''
        #Initializing the player to None
        self.player = None
    
    
    def startGame(self):
        '''
        Starts the main game loop. Welcomes the player, allows them to choose their role, 
        and repeatedly displays the main menu and takes player input until the game is exited.
        '''
        #Starting the game
        print("Welcome to Medieval Journey!")
        #Allowing the player to choose their role
        self.chooseRole()
        
        #Displaying the menu in a loop until the user quits the game
        while True:
            self.displayMenu()
            choice = input("Enter Your Choice: ").lower()
            self.choicePicked(choice)
    
    def chooseRole(self):
        '''
        Lets the player choose their role for the game. They can choose to be either a Soldier,
        a Pickpocket, or to Exit the game. Based on their choice, a respective object (either 
        Soldier or Pickpocket) is created.
        '''
        #Loop until the players makes a valid choice
        while True:
            roleChoice = input("Choose your role: 1) Soldier, 2) Pickpocket or 3) Exit? ").lower()
            if roleChoice == 'soldier' or roleChoice == '1':
                playerName = input("Enter your name:")
                #If the player chooses soldier we create a soldier object
                self.player = Soldier(playerName,self)
                break
            elif roleChoice == 'pickpocket' or roleChoice == '2':
                playerName = input("Enter your name:")
                #If the player chooses pickpocket we create a pickpocket object
                self.player = Pickpocket(playerName,self)
                break
            elif roleChoice == '3' or roleChoice == 'exit':
                #If the player chooses exit we exit the game
                print("Thanks for playing! Exiting game")
                time.sleep(1)
                exit()
            else:
                #Handling invalid choices
                print("Invalid choice!")
                
                
    def displayMenu(self):
        '''
        Displays the main menu for the game, showing various options the player can pick from.
        '''
        #Displaying the main menu
        print("\nOptions: ")
        print("1) Start Next Quest")
        print("2) Visit Shop")
        print("3) View Inventory")
        print("4) View Stats")
        print("5) Quit Game")
        
    
    def choicePicked(self, choice):
        '''
        Handles the choice picked by the player from the main menu. Executes the corresponding
        action based on the player's input.

        Args:
        - choice (str): Player's input choice (should be a string representation of a number between 1 and 5).
        '''
        #Handling the players menu choices
        if choice == '1':
            self.player.startNextQuest()
        elif choice == '2':
            self.player.visitShop()
        elif choice == '3':
            self.player.viewInventory()
        elif choice == '4':
            self.player.viewStats()
        elif choice == '5':
            #Exiting the game
            print("Thanks for playing! Exiting game")
            exit()
        else:
            #Handling invalid choices
            print("Invalid choice! Please enter a number between 1 and 5")