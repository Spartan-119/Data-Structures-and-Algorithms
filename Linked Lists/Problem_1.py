'''This program implements stacks using Linked List.'''

from logging import raiseExceptions
from xmlrpc.client import Boolean
from Node import Node
from Singly_Linked_List import SinglyLinkedList

class Stack:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        '''method to check if the stack is empty or not.'''
        if self.head == None:
            return True
        else:
            return False
        
    def push(self, data):
        '''method to push the data on to the stack.
        Note that the new node must be added to the top.
        The top is the front of the linked list.'''
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)               # creating a new node object
            new_node.next = self.head           # linking the new node to the current head
            self.head = new_node                # updating the head
    
    def pop(self):
        '''method to remove the latest, or in this implementation
        the first node of the linked list.'''
        if self.head == None:
            raise Exception('Cannot perform the pop operation. The stack is empty!')
        else:
            first_element = self.head
            self.head = first_element.next      # updating the head's link
            first_element.next = None           # disconnecting the first element from the linked list
    
    def print_stack(self):
        '''method to print all the elements in the stack.'''
        if self.head == None:
            raise Exception('NaN: The stack is empty!')    
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def peek(self):
        '''method to print the top-most element in the stack.'''
        if self.head == None:
            raise Exception('The stack is empty!')
        print(self.head.data)   
        
# the driver function
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)