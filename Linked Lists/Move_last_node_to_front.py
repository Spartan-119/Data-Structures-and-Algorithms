import imp
from Node import Node
from Singly_Linked_List import SinglyLinkedList

class MoveLastNodeToFront(SinglyLinkedList):
    def __init__(self):
        super().__init__()
    
    def move_last_to_front(self):
        first = second_last = last = self.head
        while last.next.next:
            last = last.next
            second_last = second_last.next
        last = last.next
        last.next = first                   # pointing last node's pointer to the first node
        second_last.next = None             # updating the second last node's pointer to None
        self.head = last

##########################
# Driver class
if __name__ == '__main__':
    ll = MoveLastNodeToFront()
    ll.push(6)
    ll.push(5)
    ll.push(4)                     
    ll.push(3)                      
    ll.push(2)
    ll.push(1)                      

    ll.print_list()
    print()
    ll.move_last_to_front()
    ll.print_list()

    """
    Output:
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> End

    6 -> 1 -> 2 -> 3 -> 4 -> 5 -> End
    """