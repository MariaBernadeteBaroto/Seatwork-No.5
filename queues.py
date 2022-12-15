# Building Queue Data Type

# Custom FIFO queue to support at least the enqueue and dequeue operations
# Write a bare-bones Queue class that will delegate those two operations.


from collections import deque
from heapq import heappop, heappush # Building Priority Queue Data Type
from itertools import count 

# Make the class iterable (report its length and optionally accepts initial elements)
class Queue:
    def __init__(self, *elements):
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

#Adding mixin class
class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()


#Stack(Queue) class
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

# Building Priority Queue Data Type
class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]
