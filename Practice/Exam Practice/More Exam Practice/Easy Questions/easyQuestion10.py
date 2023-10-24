#While Loops & Strings: Repeatedly ask the user to enter a word, and stop when they enter "stop".

userWord = input("Enter a word, input \"stop\" to exit ").lower()

while userWord != "stop":
    userWord = input("Enter a word, input \"stop\" to exit ").lower()
