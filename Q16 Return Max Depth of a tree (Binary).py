class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxDepth(root):
    if root == None:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    if left > right:
        return left + 1
    else:
        return right + 1

# Example tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Max depth =", maxDepth(root))