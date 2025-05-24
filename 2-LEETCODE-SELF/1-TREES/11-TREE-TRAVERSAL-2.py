# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root is None):
            return []
        ans=[]
        queue=[]
        queue.append(root)
        while(len(queue)>0):
            level=[]
            size=len(queue)
            for i in range(size):
                temp=queue.pop(0)
                level.append(temp.val)
                if(temp.left is not None):
                    queue.append(temp.left)
                if(temp.right is not None):
                    queue.append(temp.right)
            ans.append(level)
        ans=ans[::-1]
        return ans