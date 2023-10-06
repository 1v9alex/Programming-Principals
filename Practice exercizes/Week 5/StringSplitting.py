msg = "Hello World!"

''' when doing string manipulation the last value is not included in the output'''
print(msg)
#prints h
print(msg[0])
#prints Hello
print(msg[0:5])

#prints World
print(msg[6:11])

#print hell
print(msg[0:4])

#print hell World
print(msg[0:4], msg[6:11])

#get every second index in the range 0-10
print(msg[0:10:2])

#printing hello with negative index
print(msg[-12:-7])
#printing world with negative index
print(msg[-6:-1])
#printing hello world with negative index
print(msg[-12:-7], msg[-6:-1])

#printing hello world backwards
print(msg[::-1])

#printing hello world backwards with every second index
print(msg[::-2])

#print hello world 4 times
print(4*msg)

#print hello world 4 times with a space in between
print(4*msg, end="\n")

#print hello world 4 times with a new line each time
print(4*msg, end="\n")

replaced= msg.replace("Hello", "Goodbye")
print(replaced)
print(msg.find("World"))


#centering a string
print(msg.center(20, "-"))

#finding a specific value in a string
finding = "canada is a great country i love canada canada is the best, everyone should move to canada.or the united states"
print(finding.find("canada"))
print(finding.rfind("canada"))
#printing how many times canada is in the string
print(finding.count("canada"))


