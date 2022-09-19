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
            self.head = self.head.head          # updating the head's link
            first_element.next = None           # disconnecting the first element from the linked list
    


