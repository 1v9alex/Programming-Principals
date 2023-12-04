import csv
from Champion import Champion

class DataPersistenceManager:
    #load the data from the file and return it
    def loadData(self, fileName):
        champions = []
        try:
            with open(fileName, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Champion Name'].strip().title()
                    tier = row['Tier'].strip().upper()
                    difficulty = row['Difficulty'].strip().capitalize()
                    role = row['Role'].strip().capitalize()
                    champions.append(Champion(name, tier, difficulty, role))
        except Exception as e:
            print("Error loading data:", e)
        return champions

    
    
    def saveData(self,champions,fileName):
        #save the data to the file
        try:
            with open(fileName, mode='w', newline='') as file:
                fieldnames = ['Champion Name', 'Tier', 'Difficulty', 'Role']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()
                for champ in champions:
                    writer.writerow({'Champion Name': champ.getName(), 'Tier': champ.getTier(), 'Difficulty': champ.getDifficulty(), 'Role': champ.getRole()})
        except Exception as e:
            print("Error saving data:", e)

