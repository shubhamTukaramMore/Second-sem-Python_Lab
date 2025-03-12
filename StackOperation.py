class Stack:
    def __init__(self, *args):
        self.stack = list(args)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)

def main():
    stack = Stack(10, 20, 30)  # Initialize with some elements
    stack.display()  # Display stack
    stack.push(40)  # Push an element
    print("Popped:", stack.pop())  # Pop an element
    print("Top element:", stack.peek())  # Peek the top element
    stack.display()  # Display the updated stack

if __name__ == "__main__":
    main()
