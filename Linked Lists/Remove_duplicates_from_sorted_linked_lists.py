from Node import Node
from Singly_Linked_List import SinglyLinkedList

class RemoveDuplicatesSorted(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    """def check_previous(self, node):
        current = node
        node = node.next
        while node:
            if current == node:
                node = node.next"""

    
    def remove_duplicates(self) -> None:
        """since the linked list is sorted, I will use brute force and
        delete the second instance of the original data in the node.
        
        There could be one or more than one duplicates of a node's data."""

        if self.list_length() == 1:
            return None
        
        pointer_1 = pointer_2 = self.head
        while pointer_2.next:
            pointer_2 = pointer_2.next
            if pointer_2.data == pointer_1.data:
                pointer_2 = pointer_2.next
                pointer_1.next = pointer_2
            else:
                pointer_1 = pointer_2

##########################
# Driver class
if __name__ == '__main__':
    ll = RemoveDuplicatesSorted()
    ll.push(6)
    ll.push(5)
    ll.push(5)                      # first duplicate
    ll.push(4)                      
    ll.push(3)
    ll.push(3)                      # second duplicate
    ll.push(3)                      # third duplicate
    ll.push(3)                      # fourth duplicate
    ll.push(2)
    ll.push(1)                      

    ll.print_list()
    print()
    ll.remove_duplicates()
    ll.print_list()

    """
    Output:
    1 -> 2 -> 3 -> 3 -> 3 -> 3 -> 4 -> 5 -> 5 -> 6 -> End

    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> End
    """