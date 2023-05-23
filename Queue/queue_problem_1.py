'''
Problem-1 Give an algorithm for reversing a queue ܳQ.
To access the queue, we are only allowed to use the methods of queue ADT.
'''

class Stack(object):
    def __init__(self, limit = 10):
        self.stk = []
        self.limit = limit

    def is_empty(self):
        return len(self.stk) <= 0
    
    def push(self, item):
        if len(self.stk) >= self.limit:
            print('Stack Overflow!!!')
        else:
            self.stk.append(item)
        print('Stack after Push =====>')
        print(self.stk)
    
    def pop(self):
        if len(self.stk) <= 0:
            print('Stack Underflow!!!')
            return
        else:
            return self.stk.pop()
        
    def peek(self):
        if len(self.stk) <= 0:
            print('Stack Underflow!!!')
            return
        else:
            return self.stk[-1]
    
    def size(self):
        return len(self.stk)
    

# Node of a singly linked list
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        self.last = None

    # getters and setters for the data field of the node
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    # getters and setters for the next field of the node
    def set_next(self, next):
        self.next = next
    
    def get_next(self):
        return self.next
    
    # getters and setters for the last field of the node
    def set_last(self, last):
        self.last = last

    def get_last(self):
        return self.last
    
    # returns true if the node points to another node
    def has_next(self):
        return self.next != None

class Queue(object):
    def __init__(self, data = None):
        self.front = None
        self.rear = None
        self.size = 0
    
    def en_queue(self, data):
        self.lastNode = self.front
        self.front = Node(data, self.front)
        if self.lastNode:
            self.lastNode.set_last(self.front)
        if self.rear is None:
            self.rear = self.front
        self.size += 1
    
    def queue_rear(self):
        if self.rear is None:
            print('Sorry, the queueu is empty!')
            raise IndexError
        return self.rear.data
    
    def queue_front(self):
        if self.front is None:
            print('Sorry, the queue is empty!')
            raise IndexError
        return self.front.data
    
    def de_queue(self):
        if self.rear is None:
            print('Sorry, the queue is empty!')
            raise IndexError
        result = self.rear.data
        self.rear = self.rear.last
        self.size -= 1
        return result
    
    def size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
#################################

que = Queue()

for i in range(5):
    que.en_queue(i)

# suppose you have a queue myQueue
auxStack = Stack()

while not que.is_empty():
    auxStack.push(que.de_queue())

while not auxStack.is_empty():
    que.en_queue(auxStack.pop())

for i in range(5):
    print(que.de_queue())


'''
Output:
Stack after Push =====>
[0, 1]
Stack after Push =====>
[0, 1, 2]
Stack after Push =====>
[0, 1, 2, 3]
Stack after Push =====>
[0, 1, 2, 3, 4]
4
3
2
1
0
'''