# Building Queue Data Type

# Custom FIFO queue to support at least the enqueue and dequeue operations
# Write a bare-bones Queue class that will delegate those two operations.

from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    # enqueue.append() method
    def enqueue(self, element):
        self._elements.append(element)

    # dequeue.append() method
    def dequeue(self):
        return self._elements.popleft()
