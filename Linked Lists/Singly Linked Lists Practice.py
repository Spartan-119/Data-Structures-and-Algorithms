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
            #print("Node address: ", temp)
            print("Node data: ", temp.data)
            temp = temp.next
    
    # method to print the length of the list
    def listLength(self):
        current_node = self.head
        count = 1
        while(current_node.next != None):
            current_node = current_node.next
            count += 1
        return count
    
    
    # method to insert a node at a position 'pos'
    def insert_at_pos(self, pos, data):
        if self.head == None:
            print("List is empty")
        
        elif (pos > llist.listLength()):
            print("Error! Please enter a valid value for position")
            print("Cant perform the insert operation.")
            print("Returning the linked list without inserting")
            print()
        
        
        else:
            previous_node = self.head
            current_node = self.head
            count = 1
            
            
            while(count != pos):
                previous_node = current_node
                current_node = current_node.next
                count += 1
            
            new_node.next = current_node
            previous_node.next = new_node
            
        
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    new_node = Node(239)
    # now the linking part
    llist.head.next = second
    second.next = third
    
    llist.insert_at_pos(8, new_node)
    
    llist.printList()
    print("Length of the list: ", llist.listLength())
    
    
