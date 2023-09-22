'''
PROG10004 - Programming Principles, Assignment 1
Todays Date: September 22, 2023
Author: Alexander Gasee
Student Number: 991728593
Professor: Muhammad Asif
'''

#import random module
import random


#Game Title ???


#Setting up variables to be used later
playerName = ""
classChosen = ""
diceRoll = random.randint(2,12)
strength = 0
dexterity = 0
intelligence = 0
health = 0
gold = 0
luck = 0

'''
When the difficulty is set to 0, the game will be in easy mode (this will increase the stats of the player) and overall be easier
When the difficulty is set to 1, the game will be in hard mode (this will decrease the stats of the player) and overall be harder
'''
difficulty = 0

'''A 2d array of all the items currently in the players inventory
It will follow the format of [item name, item description, strength modifier, health modifier, sell value]
'''

playerInventory = []


