#Question 1 & 2
class testQueue:
    def __init__(self,c):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c
        self.count = 0

    def isFull(self):
        return self.count == self.capacity

    
    def queueEnqueue(self,data):
        if not self.isFull():
            self.queue.append(data)
            self.count += 1
    def getQueueCount(self):
        return self.count


# Question 3
class flexiQueue:
	default_size = 2
	def __init__(self):
		self.data[None]*flexiQueue.default_size
		self.front = 0
		self.size=0
	def length(self):
		return self.size

	def isEmpty(self):
		return self.size == 0
	def getfirst(self):
		if not self.isEmpty():
			return self.data[self.front]

# Question 6
class queue:
    def __init__(self):
        self.lists = []


def rotate(lists):
    output_list = []

    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])
 
    # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])
 
    return output_list		

 from queue import Queue


Question 4

from collections import deque

class Stack:

def __init__(self):

# Two inbuilt queues
self.q1 = deque()
self.q2 = deque()

def push(self, x):

# Push x first in empty q2
self.q2.append(x)

# Push all the remaining
# elements in q1 to q2.
while (self.q1):
self.q2.append(self.q1.popleft())

# swap the names of two queues
self.q1, self.q2 = self.q2, self.q1

def pop(self):

# if no elements are there in q1
if self.q1:
self.q1.popleft()

def top(self):
if (self.q1):
return self.q1[0]
return None

def size(self):
return len(self.q1)

# Driver Code
if __name__ == '__main__':
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)

print("current size: ", s.size())
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.top())

print("current size: ", s.size())


Question 5

class Queue:
def __init__(self):
self.s1 = []
self.s2 = []

def enQueue(self, x):

# Move all elements from s1 to s2
while len(self.s1) != 0:
self.s2.append(self.s1[-1])
self.s1.pop()

# Push item into self.s1
self.s1.append(x)

# Push everything back to s1
while len(self.s2) != 0:
self.s1.append(self.s2[-1])
self.s2.pop()

# Dequeue an item from the queue
def deQueue(self):

# if first stack is empty
if len(self.s1) == 0:
print("Q is Empty")

# Return top of self.s1
x = self.s1[-1]
self.s1.pop()
return x

# Driver code
if __name__ == '__main__':
q = Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)

print(q.deQueue())
print(q.deQueue())
print(q.deQueue())


