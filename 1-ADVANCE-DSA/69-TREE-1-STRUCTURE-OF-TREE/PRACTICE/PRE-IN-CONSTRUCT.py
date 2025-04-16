class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def buildTree(self,preOrder,inOrder):
        rec={val:i for i,val in enumerate(inOrder)}
        def helper(ps,pe,ios,ie):
            if(ps>pe or ios>ie):
                return None
            val=preOrder[ps]
            root=TreeNode(val)
            idx=rec[val]
            x=idx-ios
            root.left=helper(ps+1,ps+x,ios,idx-1)
            root.right=helper(ps+1+x,pe,idx+1,ie)
            return root
        return helper(0,len(preOrder)-1,0,len(inOrder)-1)
