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
    def delete(self, pos):
        if self.head == None:
            print("The list is empty")
        else:
            if (pos == 1 or pos == 0): self.pop()
            
            while
        
        '''
        elif (pos >= self.listLength()):
            while (pos > self.listLength()):
                pos = pos % self.listLength()
            if (pos == 0):
                self.pop()
            else:
                self.delete(pos)
            
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
            '''
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
    
    # Method implementing the Josephus logic
    def Josephus(self, jump):
        while (self.listLength() != 1):
            self.delete(jump)
            print("Length of the list is: ", self.listLength())
            #self.printList()
        
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
    print("Data of Node to survive is: ", cll.Josephus(2))
