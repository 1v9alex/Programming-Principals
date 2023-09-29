import random

count = 0 

while count < 10:
    print("Programming is fun!")
    count += 1
    

#random number guessing
number = random.randint(0,100)

guess = -1

print("Guess a number between 1 and 100")
while guess != number:
    guess = eval(input("Enter your guess: "))
    if guess == number:
        print("You guessed correctly! ")
    elif guess > number:
        print("You guessed too high")
    else:
        print("You guessed too low")

#Write a program to ask the user to print the next number by inputting yes or no if yes is the input print the next number otherwise stop the loop

num = 0
print(num)

while num < 10:
    nextNum = input("Do you want to print the next number, yes or no ")
    if nextNum == 'yes':
        num += 1
        print(num)
    else:
        break

#can also do like this for infinite

count = 0 
d = "yes"
print(count)
while d == "yes":
    count += 1 
    print(count)
    if count > 10:
        break

#give user 3 tries for password
count = 0
password = '1v9Alex'
validPass = False

while not validPass and count <= 3:
    p = input("Enter your password")
    if count > 3:
        print("Too many login attempts your account now will be locked for 24h")
        break
    if p != password:
        count += 1
        tries = 3 - count
        print("Incorrect Password " + str(tries) + " tries remaining")
    else:
        validPass = True
        print("You inputted the correct password, welcome")
        break

#write a program to task the user to do the transaction deposit or withdraw and keep asking if you want to do another transaction until the user inputs no, accoridng to the type of transaction update the balance

balance = 0

while True:
    # ask the user to perform a transaction
    transaction = input("Do you want to deposit or withdraw? ")
    
    # perform the transaction and update the balance
    if transaction.lower() == "deposit":
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"Deposit successful. Your new balance is {balance:.2f}")
    elif transaction.lower() == "withdraw":
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Withdrawal successful. Your new balance is {balance:.2f}")
    else:
        print("Invalid transaction type.")
    
    # ask the user if they want to perform another transaction
    another_transaction = input("Do you want to perform another transaction? (yes/no) ")
    if another_transaction.lower() == "no":
        break

print("Thank you for banking with us!")


product = 1
i = 1
while 1 < 10:
    product = product * i
    i = i + 1
print(product)


