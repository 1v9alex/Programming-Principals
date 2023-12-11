with open("Practice\Final Exam Practice\Files\Slideshow Problems\Question2\data.txt","r") as file:
    specifiedWord = "alex"
    
    a = file.readlines()
    
    testingReplace = [s.replace("alex","doesitwork") for s in a]
    


with open("Practice\Final Exam Practice\Files\Slideshow Problems\Question2\data.txt","w") as file:
    for i in testingReplace:
        file.write(i)