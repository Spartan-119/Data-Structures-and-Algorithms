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

    """def detect_loop_floyd(self) -> bool:
        '''Floyd's cycle finding algorithm:
        1. Traverse linked list using two pointers.
        2. Move one pointer(slow_p) by one and another pointer(fast_p) by two.
           If these pointers meet at the same node then there is a loop. 
        3 .If pointers do not meet then linked list doesn’t have a loop.'''
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):                          # running the while loop using the fast pointer since it'd reach the end first
            slow_p = slow_p.next                # moving the slow pointer by one
            fast_p = fast_p.next.next           # moving the fast pointer by two
            if fast_p == slow_p:
                return True
            
        return False
"""
            

##############
# the driver function
if __name__ == '__main__':
    ll = LinkedList()

    for i in range(1,6):                       # populating the linked list
        ll.push(i)
    
    ll.head.next.next.next = ll.head           # creating a loop    
    #ll.print_list()
    if ll.detect_loop():
        print('A loop is present.')
    else:
        print('No loop is present.')


'''# Python program to detect loop in the linked list

# Node class


class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print it the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

	def detectLoop(self):
		slow_p = self.head
		fast_p = self.head
		while(fast_p):
			slow_p = slow_p.next
			fast_p = fast_p.next.next
			if slow_p == fast_p:
				return 1
		return 0


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
#llist.head.next.next.next.next = llist.head
if(llist.detectLoop()):
	print("Found Loop")
else:
	print("No Loop")
'''