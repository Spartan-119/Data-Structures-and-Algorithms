from Node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def print_list(self):
        if self.detect_loop():
            raise Exception('A loop is detected in the linked list. First remove the loop from the list!')
            return None
        if self.head == None:
            return None
        current_node = self.head
        while(current_node):
            print('Node_data:', current_node.data)
            current_node = current_node.next
    
    def push(self, data):
        new_node = Node(data)                   # creating a new node using the Node object
        new_node.next = self.head
        self.head = new_node

    def detect_loop(self) -> bool:
        '''A linked list is said to have a loop if the next pointer of no node point towards None.'''
        current_node = self.head
        hash = set()
        while(current_node):            
            if current_node in hash:            # if the current node is already present in the hash
                return True                     # then return True
            hash.add(current_node)              # else add the current node to the hash
            current_node = current_node.next    # update the current node

        return False                            # return False if there is no loop

    def detect_loop_floyd(self) -> bool:
        '''Floyd's cycle finding algorithm:
        1. Traverse linked list using two pointers.
        2. Move one pointer(slow_p) by one and another pointer(fast_p) by two.
           If these pointers meet at the same node then there is a loop. 
        3 .If pointers do not meet then linked list doesn’t have a loop.'''
        slow_p = self.head
        fast_p = self.head
        while(fast_p):                          # running the while loop using the fast pointer since it'd reach the end first
            slow_p = slow_p.next                # moving the slow pointer by one
            fast_p = fast_p.next.next           # moving the fast pointer by two
            if fast_p == slow_p:
                return True
            
        return False

            

##############
# the driver function
if __name__ == '__main__':
    ll = LinkedList()

    for i in range(1,6):                       # populating the linked list
        ll.push(i)
    
    ll.head.next.next.next = ll.head           # creating a loop    
    #ll.print_list()
    if ll.detect_loop_floyd():
        print('A loop is present.')
    else:
        print('No loop is present.')
