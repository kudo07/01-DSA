from collections import defaultdict, deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self,root):
        if(not root):
            return []
        ans=defaultdict(list)
        queue=deque([root,0,0])
        # root, hd -1,0,1,  depth vertical distan 0 ,1,2 value to that node
        while(len(queue)>0):
            size=len(queue)
            for i in range(size):
                node,hd,depth=queue.pop()
                ans[hd].append((depth,node.val))
                if(node.left is not None):
                    queue.append((node.left,hd-1,depth+1))
                if(node.right is not None):
                    queue.append((node.right,hd+1,depth+1))
        result=[]
        for key in sorted(ans.keys()):
            ans[key].sort()
            # sort by node value and depth if both are same mean ans[key] which is hd and depth then value should be prioritise
            result.append([val for i,val in ans[key]])
        return result