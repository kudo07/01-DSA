class TreeNode:
    def __init__(self,val=0,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    # post order
    def make_recursive(self,root):
        if(root is None):
            return 0
        ll=self.make_recursive(root.left)
        rr=self.make_recursive
        return 1+max(ll,rr)


root=TreeNode(1)
root.left=TreeNode(3)
root.right=TreeNode(4)
sol=Solution()
print(sol.make_recursive(root))