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
    
    #Method to delete a particular Node
    def remove_node(self, node):
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while(current.next != node):
                current = current.next
            
            current.next = node.next
            if self.head == node:
                self.head = node.next
            
    # Method to return the length of the list
    def listLength(self):
        if self.head == None:
            print("The list is empty")
        else:
            current_node = self.head
            count = 1
            while(current_node.next != self.head):
                count +=1
                current_node = current_node.next
            return count
    
    # Method to get a node
    def get_node(self, index, start):
        if self.head is None:
            return None
        current = start
        for i in range(index):
            current = current.next
        return current
    
    # method to check if the CLL is left with 1 node
    def has_one_node(self, cll):
        if cll.head.next == cll.head:
            return True
        else:
            return False
    
    # Method implementing the Josephus logic
    def Josephus(self, k):
        if self.head is None:
            return None
        start = self.head
        
        while not self.has_one_node(cll):
            to_remove = self.get_node(k - 1, start)
            start = to_remove.next
            self.remove_node(to_remove)
        return self.head.data   
        
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
    
    #print("Length of the list is: ", cll.listLength())
    print("Data of Node to survive is: ", cll.Josephus(3))
