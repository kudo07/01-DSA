class Solution:
    def PreOrder(self,root):
        def answer(root,ans):
            if(root is None):
                return None
            ans.append(root.val)
            answer(root.left,ans)
            answer(root.right)
            return ans
        arr=[]
        ans=answer(root,arr)
        if(ans is None):
            return arr
        return ans