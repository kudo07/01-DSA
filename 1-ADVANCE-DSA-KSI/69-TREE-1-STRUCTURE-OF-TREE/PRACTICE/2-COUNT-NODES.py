class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    # post order
    def make_recursive(self,root):
        if(root is None):
            return 0
        ll=self.make_recursive(root.left)
        rr=self.make_recursive(root.right)
        return 1+ll+rr

root=TreeNode(1)
root.left=TreeNode(3)
root.right=TreeNode(4)
sol=Solution()
print(sol.make_recursive(root))