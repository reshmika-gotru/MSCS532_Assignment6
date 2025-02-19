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
arr.insert(500)         # Insert 500 at the end
arr.insert(2000)        # Insert 2000 at the end
arr.insert(1500, 1)      # Insert 1500 at index 1
arr.display()           # Output: [500, 1500, 2000]

print(arr.access(1))  # Output: 1500 (Access the element at index 1)
arr.delete(1)         # Delete the element at index 1
arr.display()         # Output: [500, 2000]
print(arr.access(1))  # Output: None (Index out of range)