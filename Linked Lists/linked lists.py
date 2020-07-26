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
    new_node = Node() #creating an object of the class Node using constructor
    new_node.set_data(data)
    
    if self.length == 0:
        self.head = new_node
    else:
        new_node.set_next(self.head)
        self.head = new_node
    
    self.length += 1
    
#method to insert a new node at the end of the LL
def insert_at_end(self, data):
    new_node = Node()
    new_node.set_data(data)
    
    current = self.head()
    while current.get_next() != None:
        current = current.get_next()
    
    #as soon as it reaches None do the 2 following steps
    new_node.set_next(None)
    current = new_node
    
    #increment the length of the list by 1
    self.length += 1
    
#method to insert a new node at a position 'pos'
def insert_at_pos(self, pos, data):
    if pos > self.length:
        return None
    
    elif pos == 0:
        self.insert_at_beginning(data)
    
    else:
        new_node = Node()
        new_node.set_data(data)
        
        current = self.head()
        
        # traverse to pos-1 before inserting
        while current.get_next() != pos-1:
            current.get_next()
        
        # now that you have reached pos-1
        # get ready to insert the new node at pos
        new_node.set_next(current.get_next())
        current.set_next(new_node)
        self.length += 1
