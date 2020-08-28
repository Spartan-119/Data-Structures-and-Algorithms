#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementing Stacks using Lists

Created on Fri Aug 28 12:35:43 2020

@author: Abin
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def display(self):
        return self.items
                
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
