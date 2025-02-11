class Array:
    def __init__(self):
        self.array = []

    def insert(self, value, index=None):
        """Inserts a value at a given index or at the end if no index is provided."""
        if index is None:
            self.array.append(value)
        else:
            self.array.insert(index, value)

    def delete(self, index):
        """Deletes the value at the given index."""
        if 0 <= index < len(self.array):
            del self.array[index]
        else:
            print("Index out of range")

    def access(self, index):
        """Accesses the value at the given index."""
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            print("Index out of range")
            return None

    def display(self):
        """Displays the array."""
        print(self.array)


arr = Array()
arr.insert(10)        # Insert 10 at the end
arr.insert(20)        # Insert 20 at the end
arr.insert(15, 1)     # Insert 15 at index 1
arr.display()         # Output: [10, 15, 20]

print(arr.access(1))  # Output: 15 (Access the element at index 1)
arr.delete(1)         # Delete the element at index 1
arr.display()         # Output: [10, 20]
print(arr.access(1))  # Output: None (Index out of range)