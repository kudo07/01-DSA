from collections import defaultdict, deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

class Solution:
    def BottomView(self,root):
        if(not root):
            return []
        ans=defaultdict(list)
        queue=deque([(root,0,0)])
        while(len(queue)>0):
            size=len(queue)
            node,hd,depth=queue.pop()
            ans[hd].append((depth,node.val))
            if(node.left is not None):
                queue.append((node.left,hd-1,depth+1))
            if(node.right is not None):
                queue.append((node.right,hd+1,depth+1))
        result=[]
        for key in sorted(ans.keys()):
            ans[key].sort()
            result.append(ans[key][-1][1])
        return result
    
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(10)))
root.right = TreeNode(3, TreeNode(6), TreeNode(7, None, TreeNode(8)))

sol = Solution()
print(sol.BottomView(root))