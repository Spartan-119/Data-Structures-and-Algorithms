class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

def invert_binary_tree(root):
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left

    # recursively inverting the binary tree
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root

# Example usage
# Construct a sample binary tree:
#      1
#     / \
#    2   3
#   / \
#  4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Original Tree:")
# Preorder traversal function to print the tree
def preorder(node):
    if node is not None:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

preorder(root)
print()

inverted_root = invert_binary_tree(root)

print("Inverted Tree:")
preorder(inverted_root)
