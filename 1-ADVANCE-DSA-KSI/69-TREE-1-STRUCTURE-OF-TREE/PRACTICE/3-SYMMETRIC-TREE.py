class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def isSymmetric(self.root):
        if(not root):
            return True
        return self.check(root.left,root.right)
    def check(self,r1,r2):
        if(not r1 and not r2):
            return True
        if(not r1 or not r2):
            return False
        return r1.val==r2.val and self.check(r1.left,r2.right) and self.check(r1.right,r2.left)

root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right=TreeNode(2)
root.right.left=TreeNode(4)
root.right.right=TreeNode(3)
sol=Solution()
print(sol.isSymmetric(root))


