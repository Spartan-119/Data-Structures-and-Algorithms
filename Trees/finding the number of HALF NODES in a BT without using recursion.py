class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None

def count_half_nodes(root):
    if not root:
        return 0
    
    count = 0
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node.left or node.right:
            count += 1
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return count

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left = TreeNode(7)

num_half_nodes = count_half_nodes(root)
print("Number of half nodes:", num_half_nodes)