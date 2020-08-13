# -*- coding: utf-8 -*-
"""
Josephus Problem using Circular Linked List

Created on Fri Aug 14 00:40:26 2020

@author: Abin
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        count = 0
        current = self.head
        while (current):
            print("Node: ", current.data)
            current = current.next
            count += 1
    
    #Method to delete the first Node
    def pop(self):
        if self.head == None:
            print("The list is empty")
        else:
            first_node = self.head
            current_node = self.head
            current_node = current_node.next
            
            # traverse till the last node
            while (current_node.next != self.head):
                current_node = current_node.next
            
            first_node = first_node.next
            self.head = first_node
            current_node.next = first_node
    
    #Method to delete a Node at a position 'pos'
    def delete_at_pos(self, pos):
        if self.head == None:
            print("The list is empty")
        elif (pos <= 0 or pos > cll.listLength()):
            print("Please enter a valid value of 'pos'")
        elif (pos == 1):
            cll.pop()
        else:
            count = 1
            current_node = self.head
                        
            # traverse till the position 'pos'
            while (count != pos):
                previous_node = current_node
                current_node = current_node.next
                count += 1
            
            previous_node.next = current_node.next
            current_node.next = None
    
    # Method implementing the Josephus logic
    def Josephus(self, jump):
        
        
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)
    
    # Now the linking part
    cll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh
    seventh.next = cll.head