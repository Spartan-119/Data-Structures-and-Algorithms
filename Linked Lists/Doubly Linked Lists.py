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
    
    # method to insert at the end
    def append(self, new_data):
        new_node = Node(new_data)
        
        # checking if the DLL is empty or not
        if self.head == None:
            print("The list is empty")
        else:
            # traverse till the last Node
            temp = self.head
            previous_node = self.head
            
            while (temp != None):
                previous_node = temp
                temp = temp.next
                
            
            new_node.next = None
            new_node.prev = previous_node            
            previous_node.next = new_node
            
    # method to insert at a position 'pos'
    def insert_at_pos(self, pos, new_data):
        
        new_node = Node(new_data)
        
        # checking if the list is empty or not
        if self.head == None:
            print("The list is empty")
        else:
            # traverse till the required position
            count = 0
            temp = self.head
            previous_node = self.head
            while (count != pos):
                previous_node = temp
                temp = temp.next
                count += 1
            
            prev_prev_node = previous_node.prev
            
            new_node.next = previous_node
            prev_prev_node.next = new_node
            new_node.prev = prev_prev_node
            previous_node.prev = new_node
            
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
    
    ''' PERFORMING THE OPERATIONS '''
    # pushing a node
    # dll.push(666)
    
    # appending a node
    # dll.append(555)
    
    # inserting at pos 3
    dll.insert_at_pos(3, 777)
    
    # printing the list
    dll.printList()
