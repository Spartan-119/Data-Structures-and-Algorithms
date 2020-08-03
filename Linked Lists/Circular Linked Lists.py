#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practicing CIRCULAR LINKED LISTS

יְהוָ֖ה אִ֣ישׁ מִלְחָמָ֑ה יְהוָ֖ה שְׁמֽוֹ׃

Created on Tue Aug  4 01:27:02 2020

@author: abin
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    
    ''' IN A CLL, YOU MUST ALWAYS DO
        current_node = current_node.next
        before you start the while loop '''
    
    def __init__(self):
        self.head = None
    
    # method to print the length of the list
    def listLength(self):
        if self.head == None:
            print("The list is empty")
        else:
            current_node = self.head
            count = 1
            while(current_node.next != self.head):
                count +=1
                current_node = current_node.next
            print("The length of the Circular Linked List is: ", count)
    
    # method to print the contents of the list
    def printList(self):
        if self.head == None:
            print("The list is empty")
        else:
            current_node = self.head
            print("Node: ", current_node.data)
            current_node = current_node.next
                        
            while(current_node != self.head):
                print("Node: ", current_node.data)
                current_node = current_node.next
    
    # method to append a node
    def append(self, data):
        new_node = Node(data)
        if (self.head == None):
            print("The list is empty")
        else:
            # traverse till the last node
            current_node = self.head
            previous_node = self.head
            current_node = current_node.next
            while(current_node != self.head):
                previous_node = current_node
                current_node = current_node.next
            new_node.next = self.head
            previous_node.next = new_node
            
    # method to insert a node at the beginning
    def push(self, data):
        new_node = Node(data)
        if (self.head == None):
            print("The list is empty")
        else:
            current_node = self.head
            first_node = self.head
            current_node = current_node.next
            
            # traversing till the last node
            while (current_node.next != self.head):
                current_node = current_node.next
            
            ''' Now you have reached the last node '''
            
            new_node.next = first_node            
            current_node.next = new_node
            self.head = new_node
    
if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    
    # Now Linking the Nodes
    cll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = cll.head
    
    # method to push a node
    cll.push(555)
    
    # method to append a node
    # cll.append(666)
    
    # printing the contents of the list
    cll.printList()
    
    # Printing the length of the list
    cll.listLength()