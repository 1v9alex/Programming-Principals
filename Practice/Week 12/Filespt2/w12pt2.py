with open(r"Practice\Week 12\Filespt2\testing.txt","w") as file:
    
    file.write("Alex is the best\n")
    file.write("Alex is not a human\n")
    
#write a program that reads a text file and counts the number of words in the file print the word count to the console
with open(r"Practice\Week 12\Filespt2\testing.txt","r") as file:
    wordcount = 0
    for line in file:
        words = line.split()
        wordcount += len(words)
    print(wordcount)
    

#ask the user to input a string and write the string to a file then read the file and count how many words are in the file, it should create a new file based on the users input
userinput = input("Enter a string: ")
with open(r"Practice\Week 12\Filespt2\userinput.txt","w") as file:
    file.write(userinput)
with open(r"Practice\Week 12\Filespt2\userinput.txt","r") as file:
    wordcount = 0
    for line in file:
        words = line.split()
        wordcount += len(words)
    print(wordcount)