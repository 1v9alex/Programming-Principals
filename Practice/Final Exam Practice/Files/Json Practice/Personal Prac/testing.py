import json

with open("Practice\Final Exam Practice\Files\Json Practice\Personal Prac\data.json",'a') as file:
    
    
    #random think i want to write
    data_payload = [
    {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
    'follow up': 'But enough talk!'}
    ]
    
    #writing to the file, order is what i want to write then the file
    json.dump(data_payload,file)
    
    '''
     FILE MODES
    
    R READ (DEFAULT)
    W WRITE
    X OPENS IF FOR EXCLUSIVE CREATION, WILL ONLY WORK IF FILE DOES NOT EXIST
    A APPEND
    T OPENS IN TEXT MODE
    B OPENS IN BINARY MODE
    + OPENS FOR UPDATING
    '''