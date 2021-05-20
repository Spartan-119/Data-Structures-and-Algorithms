'''
Code to find the maximum element in a binary tree
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

# recursive way to find the maximum element in a binary tree
maxData = -float("infinity")
def find_max_element(root):
    global maxData
    
    if not root: #if the root node is not present
        return maxData
    else:
        current_element = root.get_data()
        if current_element > maxData:
            maxData = current_element
        
        find_max_element(root.get_left())
        find_max_element(root.get_right())
        return maxData
    
print(find_max_element(root_node)) # prints 7
    