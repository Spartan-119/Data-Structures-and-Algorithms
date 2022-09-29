from Node import Node
from Singly_Linked_List import SinglyLinkedList

class IntersectionOfTwoSortedLinkedLists(SinglyLinkedList):
    def __init__(self):
        super().__init__()
    
    def find_intersection(self, head1, head2):                  
        """This method returns the common values in both the sorted linked lists."""
        result = []
        if head1.data >= head2.data:
            while head1.data != head2.data:
                head2 = head2.next
            
            result.append(head2.data)                               # store the first common node data

            while head1.next.data == head2.next.data:               # move both the pointers if the next
                head1 = head1.next              
                head2 = head2.next
                result.append(head2.data)                           # append the next common node data
            return result

        if head2.data >= head1.data:
            while head1.data != head2.data:
                head1 = head1.next
            
            result.append(head1.data)                               # store the first common node data

            while head1.next.data == head2.next.data:               # move both the pointers if their next node's data is same
                head1 = head1.next              
                head2 = head2.next
                result.append(head1.data)                           # append the next common node data
                if head1.next == None or head2.next == None:
                    break
            return result

        return False                                                # return False if there is no intersection


#################################################################
# Driver code
if __name__ == '__main__':
    l1 = IntersectionOfTwoSortedLinkedLists()
    l1.push(6)
    l1.push(5)
    l1.push(4)
    l1.push(3)
    l1.push(2)
    l1.push(1)
    
    l2 = IntersectionOfTwoSortedLinkedLists()
    l2.push(8)
    l2.push(5)
    l2.push(4)
    l2.push(3)

    l1.print_list()
    print()
    l2.print_list()
    print()

    linked_list = IntersectionOfTwoSortedLinkedLists()
    print(linked_list.find_intersection(l1.head, l2.head))

    """
    Output:
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> End

    3 -> 4 -> 5 -> 8 -> End

    [3, 4, 5]
    """