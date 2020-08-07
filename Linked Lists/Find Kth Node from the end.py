# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 07:13:27 2020

@author: Abin

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    # method to find the Kth node from the last node
    def find_k_from_last(self, k):
        if self.head == None:
            return None
        elif k < 0:
            return None
        elif k > sll.listLength():
            return None
        else:
            count = 1
            temp = self.head
            while (count != (sll.listLength() -k)):
                temp = temp.next
                count += 1
            return temp.data
            
    # Method to return the length of the list
    def listLength(self):
        count = 0
        temp = self.head
        while (temp != None):
            temp = temp.next
            count += 1
        return count
    
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
    print("Data in the Kth Node from the end is: ", sll.find_k_from_last(3))