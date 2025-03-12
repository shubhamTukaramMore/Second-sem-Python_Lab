def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

def main():
    n = int(input("Enter the number of terms: "))
    fibonacci(n)

if __name__ == "__main__":
    main()
