#write a program to get two numbers and an operator (+, -, *, /) from the user and print the result of the operation

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*": 
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")