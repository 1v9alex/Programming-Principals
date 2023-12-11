with open("Practice\Final Exam Practice\Files\Slideshow Problems\Question1\data.txt",'r') as file:
    
    a = file.read()
    
    print(a)
    counter = 0
    
    a = file.read()
    
    x = a.split()
    
    print(len(x),"words")
    
    