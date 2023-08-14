class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

def find_deepest_node(root):
    if not root:
        return None
    
    queue = [root]
    deepest_node = None

    while queue:
        node = queue.pop(0)
        deepest_node = node

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return deepest_node


# Example usage
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

deepest = find_deepest_node(root)
if deepest:
    print("Deepest node value:", deepest.value)
else:
    print("Tree is empty")