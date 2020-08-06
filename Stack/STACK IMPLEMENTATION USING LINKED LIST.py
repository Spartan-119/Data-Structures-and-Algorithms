# -*- coding: utf-8 -*-
"""

STACK IMPLEMENTATION USING LINKED LIST
Created on Fri Aug  7 04:50:36 2020

@author: Abin
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
    
    # Method to push a new node
    # Note here that the new node must be 
    # added at the top
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    # Method to remove the top element of the stack
    # that is the current element
    def pop(self):
        if self.head == None:
            print("The stack is empty")
        else:
            first_element =  self.head
            self.head = self.head.next
            first_element.next = None
    
    # Method to returnt the head of the Node
    # OR the first top element of the Stack
    def peek(self):
        if self.head == None:
            print("The Stack is empty")
            return None
        else:
            print(self.head.data)
    
    # Method to print out the stack
    def display(self):
        if self.head == None:
            print("The Stack is empty")
        else:
            current_node = self.head
            while (current_node != None):
                print(current_node.data)
                current_node = current_node.next

''' MAIN DRIVER FUNCTION '''
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    
    # stack.peek()
    
    stack.display()