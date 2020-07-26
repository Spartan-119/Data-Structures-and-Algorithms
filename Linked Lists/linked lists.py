# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:22:42 2020

@author: Abin 
"""

class Node:
    
    #constructor
    def __init__(self):
        self.data = None
        self.next = None
    
    #set data
    def set_data(self, data):
        self.data = data
    
    # method for getting the data
    def get_data(self):
        return self.data
    
    #method for setting the next
    def set_next(self, next):
        self.next = next
    
    # method for getting the next
    def get_next(self):
        return self.next
    
    # method for checking the next
    def has_next(self):
        return self.next != None

# getting the length of the list
def list_length(self):
    count = 0
    current = self.head
    
    while current != 0:
        count += 1
        current = current.get_next()
    
    return count

# method to insert a new node at the beginning of the LL
def insert_at_beginning(self, data):
    new_node = Node() #creating an object of the class Node
    new_node.set_data(data)
    
    if self.length == 0:
        self.head = new_node
    else:
        new_node.set_next(self.head)
        self.head = new_node
    
    self.length += 1
