# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 04:21:03 2020

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
    
