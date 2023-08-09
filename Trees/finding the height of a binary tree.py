class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

def tree_height(node):
    if node is None:
        return 0
    else:
        return 1 + max(tree_height(node.left), tree_height(node.right))

################
# the driver method
if __name__ == '__main__':
    # Creating a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Calculate and print the height of the binary tree
    height = tree_height(root)
    print("Height of the binary tree:", height)