class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left, self.right = None, None
    
def are_structurally_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    
    left_identical = are_structurally_identical(root1.left, root2.left)
    right_identical = are_structurally_identical(root1.right, root2.right)

    return left_identical and right_identical


# Example usage
# Construct two binary trees
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(4)

# Check if trees are structurally identical
result = are_structurally_identical(tree1, tree2)
print(result)  # This will print True in this example