from locale import currency
from Node import Node

class SinglyLinkedList():
    def __init__(self):
        self.head = None
    
    def print_list(self):
        '''a method to print the contents of the linked list while parsing through it.'''
        if self.head ==  None:
            print("The Linked List is empty.")
        else:            
            temp = self.head            # starting from the head of the LL.
            while (temp):
                print(temp.data, end = ' -> ')
                temp = temp.next
            if temp == None:
                print("End")            
            
    def list_length(self):
        '''method to return the length of the list.'''
        current_node = self.head
        count = 1
        while(current_node.next != None):
            count += 1
            current_node = current_node.next
        return count
    
    def insert_at_beginning(self, data):
        '''method to insert a node at the beginning of the Linked List.'''
        new_node = Node()               # creating a new node
        new_node.set_data(data)

    def insert_at_end(self, data):
        '''method to insert a node at the end of the Linked List.'''
        new_node = Node()               # having the node ready for the insertion at the end.
        new_node.set_data(data)         # setting the data in the node of the linked list.

        current_node = self.head

    def reverse_list(self):
        '''creating the method to reverse the linked list iteratively.'''
        prev = None
        current = self.head
        current_next = self.head.next

        while (current):
            current.next = prev
            prev = current
            current = current_next
            if current_next:
                current_next = current_next.next
        self.head = prev                # making the last node the head.

# Running the driver class
if __name__ == '__main__':
    ll = SinglyLinkedList()
    first = ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # now linking the lists to form the linked list
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = None

    print("Length of the Singly Linked List is: ", ll.list_length())
    print()
    print("Linked List before reversal")
    ll.print_list()
    print()
    ll.reverse_list()
    print("Linked List after reversal")
    ll.print_list()
    print()