
seconds = int(input("Enter the number of seconds: "))

minutes = seconds // 60
remainingSeconds = seconds % 60
print(f"{seconds} seconds is {minutes} minutes and {remainingSeconds} seconds")