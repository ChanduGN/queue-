def testEmptyQueue():
q1 = Queues.testQueue(5)
assert (q1.getQueueCount() == 0)

def testadd():
q1 = Queues.testQueue(5)
q1.queueEnqueue(10)
q1.queueEnqueue(20)
q1.queueEnqueue(30)
assert (q1.getQueueCount() == 4)
assert( q1.isFull() == False)



#testEmptyQueue()
testadd()

def lengthlist():
	q1= queues.flexiQueue(5)
	assert(q1.length()==0)

def reverseque():
q1 = Queues.rotate([1,2,3,4,5])
assert(q1.rotate([1,2,3]==[3,2,1]))