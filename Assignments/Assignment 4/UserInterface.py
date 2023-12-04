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

        tier = self.getValidInput("Enter Tier (S to D): ", ["S", "A", "B", "C", "D"], "Tier")
        difficulty = self.getValidInput("Enter Difficulty (Easy, Medium, Hard): ", ["Easy", "Medium", "Hard"], "Difficulty")
        role = self.getValidInput("Enter Role (Top, Mid, Jungle, Support, ADC): ", ["Top", "Mid", "Jungle", "Support", "ADC"], "Role")

        return name, tier, difficulty, role
    
    def getValidInput(self, prompt, validOptions, inputType):
        while True:
            userInput = input(prompt).capitalize()
            if userInput in validOptions:
                return userInput
            else:
                print(f"Invalid {inputType}. Please enter one of the following: {', '.join(validOptions)}.")
    
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
    
    def getSearchQuery(self, filter):
        if filter == "Tier":
            return self.getValidInput("Enter the Tier you want to search for: ", ["S", "A", "B", "C", "D"], "Tier")
        elif filter == "Role":
            return self.getValidInput("Enter the Role you want to search for: ", ["Top", "Mid", "Jungle", "Support", "ADC"], "Role")
        elif filter == "Difficulty":
            return self.getValidInput("Enter the Difficulty you want to search for: ", ["Easy", "Medium", "Hard"], "Difficulty")
        else:
            return input(f"Enter the {filter} you want to search for: ").capitalize()

    
    def displaySearchResults(self,results):
        if not results:
            print("No matching champions found.")
        else:
            for champ in results:
                print(f"Name: {champ.getName()}, Tier: {champ.getTier()}, Difficulty: {champ.getDifficulty()}, Role: {champ.getRole()}")
                
        while True:
            choice = input("\nWould you like to return to the main menu? (yes/no): ").lower()
            if choice == "yes":
                return
            elif choice == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    
    def displayAllChampions(self, champions):
        # Define the order of roles
        roleOrder = ["Top", "Jungle", "Mid", "ADC", "Support"]
        sortedChampions = self.sortChampionsByRoleAndTier(champions)

        # Display champions sorted by role and then by tier
        for role in roleOrder:
            role = role.capitalize()
            if role in sortedChampions:
                print(f"\n{role}")
                for champ in sortedChampions[role]:
                    print(f"{champ.getName()}: {champ.getTier()} Tier")
                print("-" * 20)
        while True:
            choice = input("\nWould you like to return to the main menu? (yes/no): ").lower()
            if choice == "yes":
                return
            elif choice == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    
    def sortChampionsByRoleAndTier(self, champions):
        # Sort champions by role and tier
        sortedChampions = {}
        tierOrder = {"S": 1, "A": 2, "B": 3, "C": 4, "D": 5}
        for champ in champions:
            role = champ.getRole().capitalize()
            if role not in sortedChampions:
                sortedChampions[role] = []
            sortedChampions[role].append(champ)
        
        # Sort within each role by tier
        for role in sortedChampions:
            sortedChampions[role].sort(key=lambda x: tierOrder[x.getTier()])

        return sortedChampions