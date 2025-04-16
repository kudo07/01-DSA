class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def invertTree(self,root):
        if(root is None):
            return None
        x=root.left
        y=root.right
        root.left=y
        root.right=x
        self.inverTree(root.left)
        self.invertTree(root.right)
        return root
root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right=TreeNode(2)
root.right.left=TreeNode(4)
root.right.right=TreeNode(3)
sol=Solution()
print(sol.invertTree(root))


