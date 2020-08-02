#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practicing Doubly Linked Lists

Created on Tue Jul 28 19:23:44 2020

@author: abin
"""
class Node:
    
    # constructor
    def __init__(self, prev = None, next = None, data = None):
        self.prev = prev
        self.next = next
        self.data = data

class DoublyLinkedLists:
    
    # constructor
    def __init__(self):
        self.head = None
    
    ''' INSERTION OPERATIONS '''

    # method to insert at the front
    def push(self, new_data):
        new_node = Node(None, None, new_data)
        
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
        while (temp.next != None):
            print("Node: ", temp.data)
            temp = temp.next
        
if __name__ == '__main__':
    dll = DoublyLinkedLists()
    dll.head = Node(None, None, 1)
    second = Node(dll.head, None, 2)
    third = Node(second, None, 3)
    fourth = Node(third, None, 4)
    fifth = Node(fourth, None, 5)
    
    # printing the list
    dll.printList()