class Matrix:
    def __init__(self, rows, cols):
        """Initialize a matrix with the given number of rows and columns."""
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def insert(self, value, row, col):
        """Inserts a value at the specified (row, col) position."""
        if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0]):
            self.matrix[row][col] = value  # Insert value at given (row, col)
        else:
            print("Index out of range")

    def delete(self, row, col):
        """Deletes the value at the specified (row, col) position."""
        if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0]):
            self.matrix[row][col] = 0  # Set the value at (row, col) to 0 (deletion)
        else:
            print("Index out of range")

    def access(self, row, col):
        """Accesses the value at the specified (row, col) position."""
        if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0]):
            return self.matrix[row][col]  # Return the value at (row, col)
        else:
            print("Index out of range")
            return None

    def display(self):
        """Displays the matrix."""
        for row in self.matrix:
            print(row)


# Create a 3x3 matrix
matrix = Matrix(3, 3)

matrix.insert(10, 0, 0)  # Insert 10 at (0, 0)
matrix.insert(20, 1, 1)  # Insert 20 at (1, 1)
matrix.insert(30, 2, 2)  # Insert 30 at (2, 2)
matrix.display()
# Output:
# [10, 0, 0]
# [0, 20, 0]
# [0, 0, 30]

print(matrix.access(1, 1))  # Output: 20 (Access the element at (1, 1))

matrix.delete(1, 1)        # Delete the element at (1, 1)
matrix.display()
# Output:
# [10, 0, 0]
# [0, 0, 0]
# [0, 0, 30]
