class Solution:
    def buildTree(inorder,postorder):
        rec={val:i for i,val in enumerate(inorder)}
        if(not inorder or not postorder):
            return None
        root=TreeNode(postorder.pop())
        inorderidx=rec[root.val]
        root.right=self.buildTree(inorder[:inorderidx],postorder)
        root.left=self.buildTree(inorder[inorderidx+1:],postorder)
        return root