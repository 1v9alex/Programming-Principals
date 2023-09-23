import random

#Creating and initalizing the soldier class

class Soldier:
    def __init__(self, name):
        #Constructor Method
        self.name = name
        self.gold = 0
        self.health = 100
        self.damage = 2
        self.armor = 1
        self.stamina = 1
        self.items = {"Offensive": [], "Defensive": []}
        self.challenges = [
            {"name": "Battle your first dragon", "attribute": "damage"},
            {"name": "Invade your first kingdom", "attribute": "stamina"},
            {"name": "Overthrow the evil king", "attribute": "armor"},
            {"name": "Become The King", "attribute": "Damage"}
                        
                        ]
        self.shop_items = {
            "Offensive": {
                "Dragon's Tooth": 10, "Excalibur": 100, "Blade Of Steel": 5, "Blade Of The Fallen": 50, "Long Sword": 30
            },
            "Defensive": {
                "Armour Of The Gods": 80, "Boots Of Quickness": 50, "Iron Armour": 20
            }
        }
        