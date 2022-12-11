# Building Queue Data Type

# Custom FIFO queue to support at least the enqueue and dequeue operations
# Write a bare-bones Queue class that will delegate those two operations.


from collections import deque

# Make the class iterable (report its length and optionally accepts initial elements)
class Queue:
    def __init__(self, elements):
        self._elements = deque(elements)

    #report length
    def __len__(self):
        return len(self._elements)

    #make it iretable
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
            
    # enqueue.append() method
    def enqueue(self, element):
        self._elements.append(element)

    # dequeue.append() method
    def dequeue(self):
        return self._elements.popleft()
