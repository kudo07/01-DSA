class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def answer(root,ans):
            if(root is None):
                return None
            ans.append(root.val)
            answer(root.left,ans)
            answer(root.right,ans)
            return ans
        arr=[]
        ans=answer(root,arr)
        if(ans==None):
            return arr
        return ans
        
        
        