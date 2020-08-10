# -*- coding: utf-8 -*-
"""
REVERSING A LINKED LIST USING RECURSION

Created on Sun Aug  9 06:53:28 2020

@author: Abin
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    # method to REVERSE THE LINKED LIST
    def reverse_list_recursive(self, head):
        # 1st Base case
        if self.head == None:
            return head
        # 2nd Base case
        if self.head.next_node == None:
            return head
        
        # A. label the end node as the new head node
        new_head = self.reverse_list_recursive(head.next_node)
        
        # B. set the new head node's next_node to be the previous
        #    head node (which is now the end node)
        head.next_node.next_node = head
        
        # C. set the old head node's next_node to None,
        #    which makes it the end node
        head.next_node = None
        
        return new_head
        
    # Method to return the length of the list
    def listLength(self):
        count = 0
        temp = self.head
        while (temp != None):
            temp = temp.next_node
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
                current_node = current_node.next_node
    
if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    
    # Now linking the SLL
    sll.head.next_node = second
    second.next_node = third
    third.next_node = fourth
    fourth.next_node = fifth
    
    print("Length of the Singly Linked List is: ", sll.listLength())
    print("Linked List before reversal")
    sll.printList()
    print()
    sll.reverse_list_recursive(sll.head)
    print("Linked List after reversal")
    sll.printList()
