# Function to find the sum of digits of a number
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10  # Add the last digit to total
        num = num // 10  # Remove the last digit
    return total

# Input: number from user
number = int(input("Enter a number: "))

# Calculate and display the sum of digits
result = sum_of_digits(number)
print(f"The sum of digits in {number} is: {result}")
