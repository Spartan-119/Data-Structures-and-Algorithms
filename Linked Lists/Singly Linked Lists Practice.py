# -*- coding: utf-8 -*-
"""
Practicing singly Linked Lists

Author: Abin
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    # now the linking part
    llist.head.next = second
    second.next = third
    
    # now we will traverse the linked list
