class Champion:
    def __init__(self,name,tier,difficulty,role):
        self.name = name
        self.tier = tier
        self.difficulty = difficulty
        self.role = role
    
    #Getter and Setter Methods for the Champion Class
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name
    
    def getTier(self):
        return self.tier
    
    def setTier(self,tier):
        self.tier = tier
        
    def getDifficulty(self):
        return self.difficulty
    
    def setDifficulty(self,difficulty):
        self.difficulty = difficulty
        
    def getRole(self):
        return self.role
    
    def setRole(self,role):
        self.role = role