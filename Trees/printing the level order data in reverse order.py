class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def reverse_level_order(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        level_data = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)
            level_data.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.insert(0, level_data)  # Insert at the beginning to reverse order

    return result

# Creating a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Get and print the reversed level order data
reversed_level_order = reverse_level_order(root)
print("Reversed Level Order Data:", reversed_level_order)

# Output:
# Reversed Level Order Data: [[4, 5, 6, 7], [2, 3], [1]]