class Solution:
    def minDepth(self,root):
        if(root is None):
            return 0
        if(not root.left and not.right):
            return 1
        if(root.left and not root.right):
            return 1 + self.minDepth(root.left)
        if(root.left is None and root.right):
            return 1+self.minDepth(root.right)
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))
