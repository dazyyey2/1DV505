# A head-and-tail implementation of a deque

# Each node is an instance of class Node
class Node:
    def __init__(self, value, next):
        self.value = value
        self.nxt = next


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Add element n as last entry in deque
    def add_last(self, n):
        new = Node(n, None)
        if self.head is None:   # Empty queue
            self.head = new
            self.tail = new
        else:
            self.tail.nxt = new
            self.tail = new
        self.size += 1

    # Returns a string representation of the current deque content
    def __str__(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt
        s += "}"
        return s

    # True if deque empty
    def is_empty(self):
        return self.size == 0

    # Add element n as first entry in deque
    def add_first(self, n):
        pass

    # Returns (without removing) the last entry in the deque.
    # Raises IndexError when accessing empty deque.
    def get_last(self):
        pass

    # Returns (without removing) the first entry in the deque
    # Raises IndexError when accessing empty deque.
    def get_first(self):
        pass

    # Removes and returns the first entry in the deque.
    # Raises IndexError when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        pass

    # Removes and returns the last entry in the deque.
    # Raises IndexError when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        pass

    # Returns an iterator over the deque
    # allowing for simple iteration over all elements
    # Part of Lecture 6
    def __iter__(self):
        pass
