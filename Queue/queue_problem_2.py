'''
Problem-2 How can you implement a queue using two stacks?
'''

'''
Solution: The key insight is that a stack reverses order (while a queue doesn't). A sequence of elements pushed on a stack comes back in
reversed order when popped. Consequently, two stacks chained together will return elements in the same order, since reversed order reversed
again is original order.
Let S1 and S2 be the two stacks to be used in the implementation of queue. All we have to do is to define the EnQueue and DeQueue
operations for the queue.

EnQueue Algorithm
 Just push on to stack S1
Time Complexity: O(1).
DeQueue Algorithm
 If stack S2 is not empty then pop from S2 and return that element.
 If stack is empty, then transfer all elements from S1 to S2 and pop the top element from S2 and return that popped element [we
can optimize the code a little by transferring only ݊ − 1 elements from S1 to S2 and pop the ݊
௧௛
element from S1 and return that
popped element].
 If stack S1 is also empty then throw error.
Time Complexity: From the algorithm, if the stack S2 is not empty then the complexity is O(1). If the stack S2 is empty, then we need to
transfer the elements from S1 to S2. But if we carefully observe, the number of transferred elements and the number of popped elements
from S2 are equal. Due to this the average complexity of pop operation in this case is O(1). The amortized complexity of pop operation is
O(1).
'''

class Queue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, element):
        self.s1.append(element)
    
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop()
    
##############################
q = Queue()
for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())

'''
Output:
0
1
2
3
4
'''