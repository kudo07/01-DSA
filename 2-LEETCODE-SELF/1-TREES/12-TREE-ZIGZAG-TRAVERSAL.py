# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        queue=[]
        ans=[]
        c=0
        queue.append(root)
        while(len(queue)>0):
            level=[]
            size=len(queue)
            for i in range(size):
                temp=queue.pop(0)
                val=temp.val
                level.append(val)
                if(temp.left is not None):
                    queue.append(temp.left)
                if(temp.right is not None):
                    queue.append(temp.right)
            if(c%2==0):
                ans.append(level)
            else:
                level=level[::-1]
                ans.append(level)
            c+=1
        return ans


        