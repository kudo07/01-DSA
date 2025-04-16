class TreeNode:
    def __init__(self,val=0,left=None,,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def levelOrder(self,root):
        if(not root):
            return
        ans=[]
        queue=[root]
        while(queue):
            level=[]
            size=len(queue)
            for _ in range(size):
                temp=queue.pop(0)
                level.append(temp.val)
                if(temp.left):
                    queue.append(temp.left)
                if(temp.right):
                    queue.append(temp.right)
            ans.append(level)
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

solution = Solution()
print(solution.levelOrder(root))
 