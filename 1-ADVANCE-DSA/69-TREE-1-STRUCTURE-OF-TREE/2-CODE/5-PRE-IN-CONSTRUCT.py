# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        rec={val:i for i,val in enumerate(inorder)}

        # helper function
        def helper(ps,pe,ios,ioe):
            if(ps>pe or ios>ioe):
                return None
            val=preorder[ps]
            root=TreeNode(val)
            idx=rec[val]
            x=idx-ios
            root.left=helper(ps+1,ps+x,ios,idx-1)
            root.right=helper(ps+x+1,pe,idx+1,ioe)
            return root
        return helper(0,len(preorder)-1,0,len(inorder)-1)
        