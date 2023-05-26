'''
Problem-3 Show how you can efficiently implement one stack using two queues.
Analyze the running time of the stack operations
'''

'''
Solution: Yes, it is possible to implement the Stack ADT using 2 implementations of the Queue ADT. One of the queues will be used to
store the elements and the other to hold them temporarily during the pop and top methods. The push method would enque the given
element onto the storage queue. The top method would transfer all but the last element from the storage queue onto the temporary queue,
save the front element of the storage queue to be returned, transfer the last element to the temporary queue, then transfer all elements back
to the storage queue. The pop method would do the same as top, except instead of transferring the last element onto the temporary queue
after saving it for return, that last element would be discarded. Let Q1 and Q2 be the two queues to be used in the implementation of stack.
All we have to do is to define the push and pop operations for the stack.

In the algorithms below, we make sure that one queue is always empty.
Push Operation Algorithm: Insert the element in whichever queue is not empty.
1. Check whether queue Q1 is empty or not. If Q1 is empty then Enqueue the element into Q2.
2. Otherwise EnQueue the element into Q1.

Time Complexity: O(1).
Pop Operation Algorithm: Transfer ݊n - 1 elements to the other queue and delete last from queue for performing pop operation.
1. If queue Q1 is not empty then transfer ݊n - 1 elements from Q1 to Q2 and then, DeQueue the last element of Q1 and return it.
2. If queue Q2 is not empty then transfer ݊n - 1 elements from Q2 to Q1 and then, DeQueue the last element of Q2 and return it.
Time Complexity: Running time of pop operation is O(n) as each time pop is called, we are transferring all the elements from one queue to
the other. 
'''

class Queue(object):
    def __init__(self) -> None:
        self.queue = []
    
    def is_empty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.queue:
            a = self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError
    
    def size(self):
        return len(self.queue)
    
class Stack(object):
    def __init__(self) -> None:
        self.q1 = Queue()
        self.q2 = Queue()
    
    def is_empty(self):
        return self.q1.is_empty() and self.q2.is_empty()

    def push(self, item):
        if self.q2.is_empty():
            self.q1.enqueue(item)
        else:
            self.q2.enqueue(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError('The stack is empty!')
        elif self.q2.is_empty():
            while not self.q1.is_empty():
                curr =  self.q1.dequeue()
                if self.q1.is_empty():
                    return curr
                self.q2.enqueue(curr)
        else:
            while not self.q2.is_empty():
                curr = self.q2.dequeue()
                if self.q2.is_empty():
                    return curr
                self.q1.enqueue(curr)

##########################################

stack = Stack()
for i in range(5):
    stack.push(i)
for i in range(5):
    print(stack.pop())

'''
Output:
4
3
2
1
0
'''