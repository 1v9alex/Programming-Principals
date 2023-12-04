from Champion import Champion
from ChampionManager import ChampionManager
from DataPersistenceManager import DataPersistenceManager
from UserInterface import UserInterface

def main():
    manager = ChampionManager()
    ui = UserInterface()
    dataManager = DataPersistenceManager()
    
    dataFilePath = "C:\\Users\\alexg\\OneDrive\\Desktop\\Programming\\Assignments\\Assignment 4\\champions.csv"

    manager.champions = dataManager.loadData(dataFilePath)
    
    while True:
        ui.displayMenu()
        choice = ui.getUserInput()
        
        if choice == 1:
            name,tier,difficulty,role = ui.getChampionData()
            manager.addChampion(Champion(name,tier,difficulty,role))
            dataManager.saveData(manager.champions, dataFilePath)
        elif choice == 2:
            searchChoice = ui.getSearchCriteria()
            query = ui.getSearchQuery(["Name","Tier","Difficulty","Role"][searchChoice-1])
            if searchChoice == 1:
                results = manager.searchByName(query)
            elif searchChoice == 2:
                results = manager.searchByTier(query)
            elif searchChoice == 3:
                results = manager.searchByDifficulty(query)
            elif searchChoice == 4:
                results = manager.searchByRole(query)
            ui.displaySearchResults(results)
        elif choice == 3:
            name = input("Enter the name of the champion you want to update: ")
            newData = ui.getChampionData()[1:]
            manager.updateChampion(name, {'tier': newData[0], 'difficulty': newData[1], 'role': newData[2]})
        elif choice == 4:
            name = input("Enter the name of the champion you want to delete: ")
            manager.deleteChampion(name)
        elif choice == 5:
            champions = manager.getAllChampions()
            ui.displayAllChampions(champions)
        elif choice == 6:
            break
        else:
            print("Please enter a valid choice.")
            
        
    dataManager.saveData(manager.getAllChampions(), dataFilePath)
    
if __name__ == "__main__":
    main()
