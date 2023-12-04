class UserInterface:
    def displayMenu(self):
        print("\n1. Add Champion")
        print("2. Search Champion")
        print("3. Update Champion")
        print("4. Delete Champion")
        print("5. Display All Champions")
        print("6. Exit")
    
    def getUserInput(self):
        while True:
            try:
                choice = input("Enter your choice: ")
                return int(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def getChampionData(self):
        name = input("Enter Champion Name: ").title()
        tier = input("Enter Tier (S to D): ").upper()
        difficulty = input("Enter Difficulty (Easy, Medium, Hard): ").capitalize()
        role = input("Enter Role (Top, Mid, Jungle, Support, ADC): ").capitalize()
        return name, tier, difficulty, role
    
    def getSearchCriteria(self):
        print("\nSearch by: ")
        print("1. Name")
        print("2. Tier")
        print("3. Difficulty")
        print("4. Role")
        while True:
            try:
                choice = int(input("Choose a search filter: "))
                if choice in [1, 2, 3, 4]:
                    return choice
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
    
    def getSearchQuery(self,filter):
        query = input(f"Enter the {filter} you want to search for: ")
        return query
    
    def displaySearchResults(self,results):
        if not results:
            print("No matching champions found.")
        else:
            for champ in results:
                print(f"Name: {champ.getName()}, Tier: {champ.getTier()}, Difficulty: {champ.getDifficulty()}, Role: {champ.getRole()}")
    
    def displayAllChampions(self,champions):
        sortedChampions = self.sortChampionsByRoleAndTier(champions)
        for role in sortedChampions:
            print(f"\n{role.capitalize()}")
            for champ in sortedChampions[role]:
                print(f"{champ.getName()}: {champ.getTier()} Tier")
            print("-" * 20)
    
    def sortChampionsByRoleAndTier(self,champions):
        sortedChampions = {}
        for champ in champions:
            role = champ.getRole().lower()
            if role not in sortedChampions:
                sortedChampions[role] = []
            sortedChampions[role].append(champ)
            
        for role in sortedChampions:
            sortedChampions[role].sort(key=lambda x: x.getTier())
            
        return sortedChampions