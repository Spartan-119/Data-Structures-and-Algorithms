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
    
    # method to insert a node at a position 'pos'
    def insert_at_pos(self, pos, data):
        if self.head == None:
            print("List is empty")
        
        # assuming pos < length_of_list
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
    
    llist.insert_at_pos(3, new_node)
    
    llist.printList()
    
    
