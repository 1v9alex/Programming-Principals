#"Write code that helps the user create a password, the password must be atleast 8 characters long"
#make it print  that the password is valid if it meets the conditions
#now checking for a valid email too
# if there is more then 1 @ sign in the email its invalid printing if the email is invalid
email = input("Enter an email: ")
#do the loop using the find function
while email.find("@") == -1 or email.find("@") != email.rfind("@"):
    print("This email is invalid, please try again.")
    email = input("Enter an email: ")

# do the email using the count function
while email.count("@") != 1:
    print("This email is invalid, please try again.")
    email = input("Enter an email: ")
print("This email is valid.")


password = input("Enter a password: ")
while len(password) < 8 or password == '12345678':
    if password == '12345678':
        print("This password is too common, please try again.")
    elif len(password) < 8:
        print("Password is too short, please try again.")
    password = input("Enter a password: ")
print("This password is valid.")

# now checking if the user has a valid email and password printing successful signup
print("You have successfully signed up!")
