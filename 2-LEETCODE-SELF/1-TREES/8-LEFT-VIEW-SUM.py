from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # fixed from `root` to `val`
        self.left = left
        self.right = right

class Sol:
    def SumLeftView(self, root):
        if not root:
            return 0

        queue = deque([(root, False)])
        total_sum = 0

        while queue:
            node, is_left = queue.popleft()

            # Add to sum only if it is a left leaf
            if is_left and not node.left and not node.right:
                total_sum += node.val

            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))

        return total_sum

# Example usage:
if __name__ == "__main__":
    # Constructing the tree:
    #        1
    #       / \
    #      2   3
    #     /   / \
    #    4   5   6
    #         \
    #          7

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.right = TreeNode(7)

    sol = Sol()
    print(sol.SumLeftView(root))  # Output: 4 (only node 4 is a left leaf)
