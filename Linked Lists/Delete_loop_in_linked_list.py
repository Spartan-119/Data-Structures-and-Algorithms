from Node import Node
from Detect_loop_in_linked_list import LinkedList

class DeleteLoop(LinkedList):
    def __init__(self) -> None:
        super().__init__()                              # using the parent's constructor
    
    def delete_loop(self):
        if super().detect_loop():
            current_node = self.head                    # starting at the head node
            hash = set()
            while(current_node):            
                if current_node in hash:                # if the current node is already present in the hash
                    current_node.next = None            # then return True
                    break
                hash.add(current_node)                  # else add the current node to the hash
                current_node = current_node.next        # update the current node
            print('The loop is deleted.')
            #return self.print_list()
        else:
            print('No loop present.')

#########################

# creating the driver function
if __name__ == '__main__':
    ll = DeleteLoop()
    for i in range(1,6):                       # populating the linked list
        ll.push(i)
    
    ll.head.next.next.next = ll.head           # creating a loop   
    #ll.detect_loop()
    ll.delete_loop()
    ll.detect_loop()
    