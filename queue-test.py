# test FIFO queue by importing it from the local Module queues
# See how it works!

from queues import Queue

#Implementation of __iter__ and __len__ methods;

test = Queue("1st Runner Up", "2nd Runner Up", "3rd Runner Up")
print(len(test))


for element in test:
    print(element)

print(len(test))