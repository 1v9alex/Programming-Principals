class ZooAnimal:
    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.age = age


class Owl(ZooAnimal):
    def __init__(self,name,species,age,isNocturnal=True):
        super().__init__(name,species,age)
        self.isNocturnal = isNocturnal
        
    
    def displayAnimalInfo(self):
        if self.isNocturnal:
            print(f"{self.name} is a {self.species} they are {self.age} years old, {self.name} is nocturnal")
        else:
            print(f"{self.name} is a {self.species} they are {self.age} years old, {self.name} is not nocturnal")


newO = Owl("alex","green owl",13,True)

newO.displayAnimalInfo()
