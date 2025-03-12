def calculate_percentage(marks, total_marks):
    return (marks / total_marks) * 100

def main():
    marks = float(input("Enter the marks obtained: "))
    total_marks = float(input("Enter the total marks: "))
    percentage = calculate_percentage(marks, total_marks)
    print(f"The percentage of marks is: {percentage:.2f}%")

if __name__ == "__main__":
    main()
