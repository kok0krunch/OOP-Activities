# Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd_count = 0

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    
    if num % 2 != 0:
        odd_count += 1

print(f"The number of odd numbers entered is: {odd_count}")