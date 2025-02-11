class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, value):
        """Pushes a value onto the stack."""
        self.stack.append(value)  # Add value to the top of the stack

    def pop(self):
        """Pops the top value from the stack."""
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the top element
        else:
            print("Stack is empty")
            return None

    def peek(self):
        """Peeks at the top value without removing it."""
        if not self.is_empty():
            return self.stack[-1]  # Return the top element without removing it
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        """Returns True if the stack is empty, otherwise False."""
        return len(self.stack) == 0

    def display(self):
        """Displays the contents of the stack."""
        print(self.stack)


stack = Stack()
stack.push(10)   # Stack: [10]
stack.push(20)   # Stack: [10, 20]
stack.push(30)   # Stack: [10, 20, 30]

stack.display()  # Output: [10, 20, 30]

print(stack.pop())  # Output: 30 (Popped from the stack)
stack.display()  # Output: [10, 20]

print(stack.peek())  # Output: 20 (Peeks at the top value)
stack.display()  # Output: [10, 20]

print(stack.is_empty())  # Output: False (The stack is not empty)
