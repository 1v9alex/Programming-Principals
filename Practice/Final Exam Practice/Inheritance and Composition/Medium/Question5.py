class Spacecraft:
    def __init__(self,name,mission_type,launch_date):
        self.name = name
        self.mission_type = mission_type
        self.launch_date = launch_date


class MannedSpacecraft(Spacecraft):
    def __init__(self,name,mission_type,launch_date,crew_capacity):
        super().__init__(name,mission_type,launch_date)
        self.crew_capacity = crew_capacity

class UnmannedSpacecraft(Spacecraft):
    def __init__(self,name,mission_type,launch_date,research_instruments =None):
        super().__init__(name,mission_type,launch_date)
        self.research_instruments = research_instruments if research_instruments is not None else []
    
    def addInstrument(self,instrument):
        self.research_instruments.append(instrument)
        return self.research_instruments

class SpaceAgency:
    def __init__(self):
        self.fleet = []
    
    def addSpacecraft(self,spacecraft:Spacecraft):
        self.fleet.append(spacecraft)
        return self.fleet
    
    def decommission_spacecraft(self, spacecraft:Spacecraft):
        if spacecraft in self.fleet:
            self.fleet.remove(spacecraft)

    def display_fleet(self):
        for spacecraft in self.fleet:
            print(spacecraft.name)


agency = SpaceAgency()
apollo = MannedSpacecraft("Apollo 11", "Lunar Landing", "1969-07-16", 3)
voyager = UnmannedSpacecraft("Voyager 1", "Interstellar Exploration", "1977-09-05")

agency.addSpacecraft(apollo)
agency.addSpacecraft(voyager)

agency.display_fleet()