#function of find the GCD of two Numbers
# Function to find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input: two positive numbers
num1 = int(input("Enter the first positive number: "))
num2 = int(input("Enter the second positive number: "))

# Ensure that the numbers are positive
if num1 <= 0 or num2 <= 0:
    print("Please enter positive numbers.")
else:
    # Calculate and display the GCD
    result = gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {result}")
