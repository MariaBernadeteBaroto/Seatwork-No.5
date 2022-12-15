# test FIFO queue by importing it from the local Module queues
# See how it works!

from queues import Queue
from queues import Stack
from queues import PriorityQueue

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
heappush(fruits, "orange")
heappush(fruits, "apple")


#implemented heappop
from heapq import heappop
heappop(fruits)

print(fruits)

#-------------------------------
#Priority Queue Data Type
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT,"windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

print(messages.dequeue())
