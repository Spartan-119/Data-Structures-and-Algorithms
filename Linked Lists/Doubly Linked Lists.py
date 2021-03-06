#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practicing Doubly Linked Lists

Created on Tue Jul 28 19:23:44 2020

יְהוָ֖ה אִ֣ישׁ מִלְחָמָ֑ה יְהוָ֖ה שְׁמֽוֹ׃

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
    
    ''' PRINTING THE LENGTH OF THE LIST '''
    def listLength(self):
        if self.head == None:
            print("The list is empty")
        else:
            count = 0
            temp = self.head
            while (temp != None):
                temp = temp.next
                count += 1
            print("Length of the DLL: ", count)
    
    
    ''' DELETION OPERATIONS '''
    
    # method to delete the node at the beginning
    def pop(self):
        temp = self.head
        self.head = temp.next
        temp.prev = None
        temp.next = None
        self.head.prev = None
    
    # method to delete at the end
    def delete_at_end(self):
        temp = self.head
        
        # traverse till  the end
        while (temp.next != None):
            previous_node = temp
            temp = temp.next
        
        previous_node.next = None
    
    # method to delete a node at position 'pos'
    def delete_at_pos(self, pos):
        count = 1
        previous_node = self.head
        current_node = self.head
        
        # traverse till pos
        while (count < pos):
            previous_node = current_node
            current_node = current_node.next
            count += 1
        
        next_node = current_node.next
        previous_node.next = next_node
        next_node.prev = previous_node
        
    
    
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
    
    ''' PERFORMING INSERTION & DELETION OPERATIONS '''
    # pushing a node
    # dll.push(666)
    
    # appending a node
    # dll.append(555)
    
    # inserting at pos 3
    # dll.insert_at_pos(3, 777)
    
    # deleting the node at the beginning
    # dll.pop()
    
    # deleting at the end
    # dll.delete_at_end()
    
    # deleting at pos 3
    # dll.delete_at_pos(3)
    
    # printing the list
    dll.printList()
    
    #printing the list length
    dll.listLength()
