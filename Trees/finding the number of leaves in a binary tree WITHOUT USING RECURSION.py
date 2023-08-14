"""
A node with two empty subtrees is called a leaf.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

def count_leaves(root):
    if root is None:
        return 0
    
    count = 0
    stack = [root]

    while stack:
        node = stack.pop(0)
        if node.left is None and node.right is None:
            count += 1

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return count

# Example usage
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

num_leaves = count_leaves(root)
print("Number of leaves:", num_leaves)