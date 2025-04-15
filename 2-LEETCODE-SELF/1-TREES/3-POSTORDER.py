class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def answer(root,ans):
            if(root is None):
                return None
            answer(root.left,ans)
            answer(root.right,ans)
            ans.append(root.val)
            return ans
        arr=[]
        ans=answer(root,arr)
        if(ans==None):
            return arr
        return ans
        