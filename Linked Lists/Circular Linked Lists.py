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
    
    def __init__(self):
        self.head = None
    
    def printList(self):
        if self.head == None:
            print("The list is empty")
        else:
            current_node = self.head
            count = 1
            while(current_node.next != self.head):
                count +=1
                current_node = current_node.next
            print("The length of the Circular Linked List is: ", count)

if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    
    # Now Linking the Nodes
    cll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = cll.head
    
    # Printing the length of the list
    cll.printList()
