# -*- coding: utf-8 -*-
"""

STACK IMPLEMENTATION USING LINKED LIST
Created on Fri Aug  7 04:50:36 2020

@author: HCL
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    # method to check if the Stack is empty or not
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False