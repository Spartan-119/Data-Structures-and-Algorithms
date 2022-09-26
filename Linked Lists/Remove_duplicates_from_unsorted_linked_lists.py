from Node import Node
from Singly_Linked_List import SinglyLinkedList

class RemoveDuplicatesUnsorted(SinglyLinkedList):
    def __init__(self):
        super().__init__()
    
    def remove_duplicates(self):
        current_node = self.head
        data_hash = set()
        while current_node.next:
            if current_node.next.data in data_hash:
                current_node.next = current_node.next.next
            else:
                data_hash.add(current_node.next.data)
                current_node = current_node.next


##########################
# Driver class
if __name__ == '__main__':
    ll = RemoveDuplicatesUnsorted()
    ll.push(6)
    ll.push(56)
    ll.push(55)                      
    ll.push(41)                      
    ll.push(30)
    ll.push(38)                      
    ll.push(55)                      
    ll.push(2)                      
    ll.push(6)                       
    ll.push(100)                      

    ll.print_list()
    print()
    ll.remove_duplicates()
    ll.print_list()

    """
    Output:
    100 -> 6 -> 2 -> 55 -> 38 -> 30 -> 41 -> 55 -> 56 -> 6 -> End

    100 -> 6 -> 2 -> 55 -> 38 -> 30 -> 41 -> 56 -> End"""