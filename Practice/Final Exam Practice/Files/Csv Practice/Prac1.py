with open("Practice\Final Exam Practice\Files\Csv Practice\data.csv", "r") as c:
    
    for line in c:
        values = line.strip().split(",")
        
        print(values)