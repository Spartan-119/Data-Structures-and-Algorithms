# -*- coding: utf-8 -*-
"""
Circular Array Implementation in Queue

@author: Abin
"""
class Queue:
    def __init__(self, limit = 5):
        self.q = []
        self.limit = limit
        self.front = None
        self. rear = None
        self.size = 0
        
    def is_empty(self):
        return self.size <= 0
    
    def Enqueue(self, item):
        if self.size >= self.limit:
            print("Queue overflow exception!")
            return
        else:
            self.q.append(item)
        
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        
        self.size += 1
        
        print("Queue after Enqueue: ", self.q)
    
    def Dequeue(self):
        if self.size < 0:
            print("Queue Underflow Exception!")
            return -1
        else:
            self.q.pop(0)
            self.size -= 1
            
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
            print("Queue after Dequeue: ", self.q)