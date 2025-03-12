def sum_of_even_numbers(limit):
    even_sum = 0
    for number in range(2, limit + 1, 2):
        even_sum += number
    return even_sum

def sum_of_odd_numbers(limit):
    odd_sum = 0
    for number in range(1, limit + 1, 2):
        odd_sum += number
    return odd_sum

def main():
    limit = int(input("Enter a number: "))
    
    even_sum = sum_of_even_numbers(limit)
    odd_sum = sum_of_odd_numbers(limit)
    
    print(f"The sum of even numbers up to {limit} is: {even_sum}")
    print(f"The sum of odd numbers up to {limit} is: {odd_sum}")

#Question arise here
if __name__ == "__main__":
    main()