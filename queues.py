class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []

    def enqueue(self, value):
        """Adds a value to the back of the queue."""
        self.queue.append(value)  # Add value to the end of the queue

    def dequeue(self):
        """Removes and returns the front value from the queue."""
        if not self.is_empty():
            return self.queue.pop(0)  # Remove and return the front element
        else:
            print("Queue is empty")
            return None

    def front(self):
        """Peeks at the front value without removing it."""
        if not self.is_empty():
            return self.queue[0]  # Return the front element without removing it
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        """Returns True if the queue is empty, otherwise False."""
        return len(self.queue) == 0

    def display(self):
        """Displays the contents of the queue."""
        print(self.queue)


queue = Queue()
queue.enqueue(10)   # Queue: [10]
queue.enqueue(20)   # Queue: [10, 20]
queue.enqueue(30)   # Queue: [10, 20, 30]

queue.display()  # Output: [10, 20, 30]

print(queue.dequeue())  # Output: 10 (Dequeued from the queue)
queue.display()  # Output: [20, 30]

print(queue.front())  # Output: 20 (Peeks at the front value)
queue.display()  # Output: [20, 30]

print(queue.is_empty())  # Output: False (The queue is not empty)
