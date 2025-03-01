# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

total_sum = 0

# Loop to get 10 numbers from the user
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    total_sum += num  # Add the number to the total sum

# Print the total sum
print(f"The sum of all 10 numbers is: {total_sum}")