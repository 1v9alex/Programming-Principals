import json

with open("Practice\Final Exam Practice\Files\Json Practice\Personal Prac\data.json") as file:
    
    #this turns it into a dictionary
    message = json.load(file)
    
    # reading a specific key from the dictionary
    print(message["name"])
    
    #prnting the whole dict
    print(message)