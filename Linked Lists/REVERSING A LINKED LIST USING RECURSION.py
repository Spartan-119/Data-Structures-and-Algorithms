# -*- coding: utf-8 -*-
"""
REVERSING A LINKED LIST USING RECURSION

Created on Sun Aug  9 06:53:28 2020

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
    def reverse(self, current, previous):
        next = current.next
        current.next = previous
        if next is None:
            return current
        else:
            self.reverse(next, current)
        
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
                print("Node: ", current_node.data)
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
    print("Linked List before reversal")
    sll.printList()
    print()
    sll.reverse(sll.head, None)
    print("Linked List after reversal")
    sll.printList()