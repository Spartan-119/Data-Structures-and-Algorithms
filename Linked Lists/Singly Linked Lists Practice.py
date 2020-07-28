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
        
        elif (pos > llist.listLength() or pos <= 0):
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
    
    '''  DELETING THE NODES '''
    # Method to delete the node at the beginning
    def delete_at_beginning(self):
        temp = self.head
        temp = temp.next
        self.head.next = None
        self.head = temp
    
    # Method to delete the node at the end
    def delete_at_end(self):
        temp = self.head
        
        # traverse till  the end
        while (temp.next != None):
            previous_node = temp
            temp = temp.next
        
        previous_node.next = None
    
    # Method to delete the Node at a position 'pos'
    def delete_at_pos(self, pos):
        count = 1
        temp = self.head
        
        # traverse till pos
        while (count != pos):
            previous_node = temp
            temp = temp.next
            count += 1
        
        # first connect the previous node's link to the next
        # node
        previous_node.next = temp.next
        temp.next = None
    
    
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    
    # Inserting the new node
    new_node = Node(239)
    
    # now the linking part
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    
    # Method to insert a new node at a position 'pos'
    #llist.insert_at_pos(0, new_node)
    
    # deleting the node at the beginning
    #llist.delete_at_beginning()
    
    # deleting the node at the end
    #llist.delete_at_end()
    
    # deleting the node at a position 'pos'
    #llist.delete_at_pos(2)
    
    llist.printList()
    print("Length of the list: ", llist.listLength())
    
    
