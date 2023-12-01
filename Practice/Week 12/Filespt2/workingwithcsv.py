import csv

# Add a new champion to the CSV file
with open(r"Practice\Week 12\Filespt2\testing.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["NewChampion", "NewRole", "NewDifficulty"])

# Print all the champions and their roles and difficulties
with open(r"Practice\Week 12\Filespt2\testing.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader, None)
    
    if header is None:
        print("File is empty")
    else:
        for row in reader:
            if len(row) < 3:  # Check if the row has enough columns
                print("Invalid row:", row)
            else:
                print(f"Champion: {row[0]}, Role: {row[1]}, Difficulty: {row[2]}")