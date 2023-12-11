with open("Practice\Final Exam Practice\Files\Slideshow Problems\Question3\data.txt","r") as file:
    
    word_freq = {}
    
    for line in file:
        words = line.split()
        
        for word in words:
            word = word.strip(".,!?").lower()
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
                
    for word, freq in word_freq.items():
        print(f"'{word}': {freq}")