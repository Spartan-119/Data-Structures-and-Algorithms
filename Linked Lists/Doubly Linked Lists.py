#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practicing Doubly Linked Lists

Created on Tue Jul 28 19:23:44 2020

@author: abin
"""
class Node:
    
    # constructor
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class DoublyLinkedLists:
    
    # constructor
    def __init__(self):
        self.head = None
    
    ''' INSERTION OPERATIONS '''

    # method to insert at the front
    def push(self, new_data):
        new_node = Node(new_data)
        
        # checking if the DLL is empty or not
        if self.head == None:
            print("The list is empty")
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
    
    ''' PRINTING THE LIST '''
    def printList(self):
        temp = self.head
        while (temp != None):
            print("Node: ", temp.data)
            temp = temp.next
        
if __name__ == '__main__':
    dll = DoublyLinkedLists()
    dll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    
    # now the linking part
    dll.head.prev = None
    dll.head.next = second
    
    second.prev = dll.head
    second.next = third
    
    third.prev = second
    third.next = fourth
    
    fourth.prev = third
    fourth.next = fifth
    
    fifth.prev = fourth
    fifth.next = None
    
    # printing the list
    dll.printList()
