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
    
    #traversing through the list while printing
    def printList(self):
        temp = self.head # starting from head
        while(temp):
            print("Node address: ", temp)
            print("Node data: ", temp.data)
            temp = temp.next
        
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    # now the linking part
    llist.head.next = second
    second.next = third
    
    llist.printList()
    
    
