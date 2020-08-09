# -*- coding: utf-8 -*-
"""
REVERSING A LINKED LIST USING ITERATION

Created on Sat Aug  8 14:44:33 2020

@author: Abin
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    # method to REVERSE THE LINKED LIST
    def reverse_list_iterative(self):
        prev = None
        current = self.head
        following = current.next
        while (current):
            current.next = prev
            prev = current
            current = following
            if following:
                following = following.next
        self.head = prev
    
            
    # Method to return the length of the list
    def listLength(self):
        count = 0
        temp = self.head
        while (temp != None):
            temp = temp.next
            count += 1
        return count
    
    # Method to print the list
    def printList(self):
        if self.head ==  None:
            print("The list is empty")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data, end = " -> ")
                current_node = current_node.next
    
if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    
    # Now linking the SLL
    sll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    
    print("Length of the Singly Linked List is: ", sll.listLength())
    print()
    print("Linked List before reversal")
    sll.printList()
    print()
    print()
    sll.reverse_list_iterative()
    print("Linked List after reversal")
    sll.printList()
