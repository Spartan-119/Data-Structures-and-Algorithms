"""
in the context of a binary tree,
the size of a binary tree is the total number of nodes present in the tree,
including both internal nodes and leaf nodes.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_size(node):
    if node is None:
        return 0
    else:
        return 1 + tree_size(node.left) + tree_size(node.right)
    
if __name__ == "__main__":
    # creating a binary tree
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(6)

    # calculate the size of the binary tree
    size = tree_size(root)
    print(f"The size of the binary tree is {size}.")