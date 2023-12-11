import csv

with open("Practice\Final Exam Practice\Files\Slideshow Problems\Question5\data.csv","r") as input_file, open("Practice\Final Exam Practice\Files\Slideshow Problems\Question5\data2.csv","w",newline = '') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    
    header_row = next(reader)
    writer.writerow(header_row)
    
    for row in reader:
        salary = float(row[2])
        
        if salary > 50000:
            writer.writerow(row)
