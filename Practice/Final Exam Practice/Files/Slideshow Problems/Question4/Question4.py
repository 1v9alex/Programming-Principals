with open("Practice\Final Exam Practice\Files\Slideshow Problems\Question4\data.txt","r") as file:
    
    longestWord = ""
    secondLongestWord = ""
    for line in file:
        words = line.split()
        
        for word in words:
            word = word.strip(".,!?").lower()
            
            if len(word) > len(longestWord):
                longestWord = word
            elif len(word) < len(longestWord) and  len(word) > len(secondLongestWord):
                secondLongestWord = word
    
    print(longestWord)
    print(secondLongestWord)
            