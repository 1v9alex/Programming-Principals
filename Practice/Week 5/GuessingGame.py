
guessNum = 20


print("Guess a number between 1 and 100 ")

guess = -1
counter = 0
while guess != guessNum:
    guess = int(input("Enter your guess! "))
    counter += 1
    if guess == guessNum:
        print("Correct the number is", guessNum)
        print("It took you ",counter, " tries")  
    elif guess > guessNum:
        print("Try a lower number ")
    else:
        print("Try a higher number ")
    