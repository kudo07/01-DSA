from collections import defaultdict, deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
class Solution:
    def TopView(self,root):
        if(not root):
            return []
        ans=defaultdict(list)
        queue=deque([(root,0,0)])
        top=[]
       
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
            print(ans[key])
            result.append(ans[key][0][1])
            # result.append([val for i,val in ans[key]])
        return result
        
            
        

    

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(10)))
root.right = TreeNode(3, TreeNode(6), TreeNode(7, None, TreeNode(8)))

sol = Solution()
print(sol.TopView(root))