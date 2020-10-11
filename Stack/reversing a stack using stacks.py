# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:40:45 2020

@author: Abin
"""
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def reverse(self):
        new_stack = []
        for i in range(0, len(self.stack)):
            new_stack.append(self.stack.pop())
        
        return new_stack
    
    def show(self):
        return self.stack
    
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    
    print("Original stack: ", s.show())
    print("Reversed stack using stacks: ", s.reverse())