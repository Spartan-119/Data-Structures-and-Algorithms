'''
code to search for an element
in a binary tree
RECURSIVE way
'''

class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    

# inserting data into the nodes
root_node = BinaryTreeNode(1)
root_node.left = BinaryTreeNode(2)
root_node.right = BinaryTreeNode(3)
root_node.left.left = BinaryTreeNode(4)
root_node.left.right = BinaryTreeNode(5)
root_node.right.left = BinaryTreeNode(6)
root_node.right.right = BinaryTreeNode(7)

def find_element(root, data):
    if not root:
        return 0
    
    if root.get_data() == data:
        return 1
    else:
        temp = find_element(root.get_left(), data)
        if temp == 1:
            return temp
        else:
            return find_element(root.get_right(), data)

        
print(find_element(root_node, 5)) # returns 1