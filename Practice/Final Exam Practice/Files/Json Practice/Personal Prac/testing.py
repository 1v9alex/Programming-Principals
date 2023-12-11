import json

with open("Practice\Final Exam Practice\Files\Json Practice\Personal Prac\data.json",'a') as file:
    
    
    
    data_payload = [
    {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
    'follow up': 'But enough talk!'}
    ]
    
    json.dump(data_payload,file)