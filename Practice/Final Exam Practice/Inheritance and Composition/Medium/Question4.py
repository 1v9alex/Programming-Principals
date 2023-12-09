class Plant:
    def __init__(self,species,height,growth_rate):
        self.species = species
        self.height = height
        self.growth_rate = growth_rate


class Flower(Plant):
    def __init__(self,species,height,growth_rate,flower_color):
        super().__init__(species,height,growth_rate)
        self.flower_color = flower_color
    
    
    def displayInfo(self):
        print(f"Species: {self.species} Height: {self.height}cm Growth Rate: {self.growth_rate}cm/d Color: {self.flower_color}")
        

newF = Flower("Sunflower",100,10,"Yellow")

newF.displayInfo()