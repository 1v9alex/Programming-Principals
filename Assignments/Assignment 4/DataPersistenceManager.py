import csv
from Champion import Champion

class DataPersistenceManager:
    def loadData(self,fileName):
        champions = []
        try:
            with open(fileName, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    champions.append(Champion(row['Champion Name'], row['Tier'], row['Difficulty'], row['Role']))
        except Exception as e:
            print("Error loading data:", e)
        return champions
    
    
    def saveData(self,champions,fileName):
        try:
            with open(fileName, mode='w', newline='') as file:
                fieldnames = ['Champion Name', 'Tier', 'Difficulty', 'Role']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()
                for champ in champions:
                    writer.writerow({'Champion Name': champ.getName(), 'Tier': champ.getTier(), 'Difficulty': champ.getDifficulty(), 'Role': champ.getRole()})
        except Exception as e:
            print("Error saving data:", e)

