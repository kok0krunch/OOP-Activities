# Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 ** num2

print(f"{num1} raised to the power of {num2} is: {result}")