# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:22:42 2020

@author: HCL
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