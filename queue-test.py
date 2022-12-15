# test FIFO queue by importing it from the local Module queues
# See how it works!

from queues import Queue
from queues import Stack

#Implementation of __iter__ and __len__ methods;

test = Queue("1st Runner Up", "2nd Runner Up", "3rd Runner Up")
print(len(test))


for element in test:
    print(element)

print(len(test))

#test stack class
test2 = Stack("1st Runner Up", "2nd Runner Up", "3rd Runner Up")
for element in test2:
    print(element)

#using heapq module
from heapq import heappush

fruits = []
veges = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(veges, "squash")

print(fruits)
print(veges)