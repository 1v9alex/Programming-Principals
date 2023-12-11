import csv

with open("Practice\Final Exam Practice\Files\Csv Practice\data.csv", "w",newline="") as file:
    
    csv_writer = csv.writer(file)
    
    csv_writer.writerow(["name","age","city"])
    csv_writer.writerow(["alex",18,"canada"])
    csv.writer(file).writerow(["Alexander",18,"Canada"])