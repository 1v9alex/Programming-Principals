class ChampionManager:
    def __init__(self):
        self.champions = []
        
    def addChampion(self,champion):
        #add a new champion object to the champions list
        self.champions.append(champion)
    
    def deleteChampion(self,name):
        '''
        Remove a champion from the list by name
        Its done by filtering out the champion whose name matches the one that user will input later
        '''
        self.champions = [champ for champ in self.champions if champ.getName() != name]
    
    def updateChampion(self,name,newData):
        '''
        Update the attributes of an existing champion based on user input later
        It searches for the champion by name and updates its data
        '''
        for champ in self.champions:
            if champ.getName().lower() == name.lower():  # Case-insensitive comparison
                champ.setTier(newData['tier'])
                champ.setDifficulty(newData['difficulty'])
                champ.setRole(newData['role'])
                return True
        return False  # Return False if the champion is not found
    
    def championExists(self, name):
        return any(champ.getName().lower() == name.lower() for champ in self.champions)
    
    def searchByName(self, name):
        '''
        Searches for champions by name and returns a list of matching champions.
        Could return multiple champions if there are duplicates with the same name.
        '''
        return [champ for champ in self.champions if champ.getName() == name]

    def searchByTier(self, tier):
        '''
        Searches for champions by tier and returns a list of matching champions.
        Champions with the specified tier will be returned.
        '''
        return [champ for champ in self.champions if champ.getTier() == tier]

    def searchByDifficulty(self, difficulty):
        '''
        Searches for champions by difficulty and returns a list of matching champions.
        Champions with the specified difficulty will be returned.
        '''
        return [champ for champ in self.champions if champ.getDifficulty() == difficulty]

    def searchByRole(self, role):
        '''
        Searches for champions by role and returns a list of matching champions.
        Champions with the specified role will be returned.
        '''
        return [champ for champ in self.champions if champ.getRole() == role]
    
    def getAllChampions(self):
        #gets all champions
        return self.champions