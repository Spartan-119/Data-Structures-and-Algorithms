class Queue(object):
    def __init__(self, limit = 5) -> None:
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    
    def is_empty(self):
        return self.size <= 0
    
    # sicne this is a circular array implementation, we must resize the array upon enqueing and dequeueing
    def resize(self):
        new_que = list(self.que)
        self.limit = 2 * self.limit             # extending the limit of the queue to potentially accommodate more items
        self.que = new_que
    
    def en_queue(self, item):
        if self.size >= self.limit:
            self.resize()
        self.que.append(item)

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        print('Queue after en_queue', self.que)
    
    def de_queue(self):
        if self.size <= 0:
            print('Queue Underflow!')
            return None
        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
            print('Queue after de_queue', self.que)
    
    def queue_rear(self):
        if self.rear is None:
            print('Sorry, the queue is empty!')
            raise IndexError
        return self.que[self.rear]
    
    def queue_front(self):
        if self.front is None:
            print('Sorry, the queue is empty!')
            raise IndexError
        return self.que[self.front]
    
    def size(self):
        return self.size
    

# creating the class
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

que.en_queue('fourth')
print('Front:', que.queue_front())
print('Rear:', que.queue_rear())

que.en_queue('fifth')
print('Front:', que.queue_front())
print('Rear:', que.queue_rear())

que.en_queue('sixth')
print('Front:', que.queue_front())
print('Rear:', que.queue_rear())

que.de_queue()                                      # de_queueing operation
print('Front:', que.queue_front())
print('Rear:', que.queue_rear())

que.de_queue()                                      # de_queueing operation [AGAIN]
print('Front:', que.queue_front())
print('Rear:', que.queue_rear())