"""
Those nodes in the tree which have both the children are known as full nodes.
"""
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None

def count_full_nodes(root):
    if root is None:
        return 0
    
    count = 0
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node.left and node.right:
            count += 1
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return count

# Example usage
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(7)

num_full_nodes = count_full_nodes(root)
print("Number of full nodes:", num_full_nodes)