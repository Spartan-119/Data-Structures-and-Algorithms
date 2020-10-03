# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 00:49:25 2020

@author: AI Learnings
"""
class SmartStack:
    def __init__(self):
        self.stack = []
        self.min = []
    
    def stack_min(self):
        return self.min[-1]
    
    def stack_pop(self):
        x = self.stack.pop()
        self.min.pop()
        return x
    
    def stack_push(self, item):
        self.stack.append(item)
        if not self.min or item <= self.stack_min():
            self.min.append(item)
        else:
            self.min.append(self.min[-1])
            
# DRIVER CLASS
# I HAVE PRECODED IT TO SAVE SOME TIME
if __name__ == "__main__":
    s = SmartStack()
    s.stack_push(2)
    s.stack_push(4)
    s.stack_push(6)
    s.stack_push(1)
    s.stack_push(5)
    print(s.stack_min())

