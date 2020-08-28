#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implemented Stacks using Lists
Use stacks for checking balancing of symbols

Created on Thu Aug 27 09:20:00 2020

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
open_list = ["(", "{", "["]
close_list = [")", "}", "]"]

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def check(myStr):
    s = Stack()
    is_balanced = True
    index = 0
    
    while(index < len(myStr) and is_balanced):
        symbol = myStr[index]
        if symbol in open_list:
            s.push(symbol)
        else:
            top = s.pop()
            if not  is_match(top, symbol):
                is_balanced = False
        
        index += 1
    
    if s.is_empty() and is_balanced:
        return True
    else:
        return False

string = "()(()[()])"
print(check(string))
