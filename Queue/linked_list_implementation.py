# Node of a singly linked list
class Node:
    '''
    Here, in this implementation, the data can be modified through the constructor and the getters and setters.
    '''
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next
        self.last = None
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_next(self, next):
        self.next = next
    
    def get_next(self):
        return self.next

    def set_last(self, last):
        self.last = last
    
    def get_last(self):
        return self.last
    
    def has_next(self) -> bool:
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
            print('Sorry, the queue is empty!')
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
    
##########################

que = Queue()
que.en_queue('first')
print('Front:', que.queue_front())
print('Rear:', que.queue_rear())

que.en_queue('second')
print('Front:', que.queue_front())
print('Rear:', que.queue_rear())

que.en_queue('third')
print('Front:', que.queue_front())
print('Rear:', que.queue_rear())

print()

print('DEQUEUEING =====>')
que.de_queue()
print('Front:', que.queue_front())
print('Rear:', que.queue_rear())