# test FIFO queue by importing it from the local Module queues
# See how it works!

from queues import Queue

test = Queue()
test.enqueue("1st Runner Up")
test.enqueue("2nd Runner Up")
test.enqueue("3rd Runner Up")

print(test.dequeue())
print(test.dequeue())
print(test.dequeue())
