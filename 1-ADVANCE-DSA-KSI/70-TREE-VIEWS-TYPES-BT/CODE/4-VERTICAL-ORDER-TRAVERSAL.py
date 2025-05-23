# class Solution:
#     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#         mapp=defaultdict(list)
#         def preOrder(root,dist):
#             if(root is None):
#                 return None

#             mapp[dist].append(root.val)
#             preOrder(root.left,dist-1)
#             preOrder(root.right,dist+1)
#         ans=preOrder(root,0)
#         print(ans,mapp)
# {0: [9, 3, 8, 12], -1: [6, 20, 11, 5], -2: [2, 14], -3: [7], 1: [7, 1], 2: [1]})
# RELATIVE ANSWER IS NOT CORRECT
# WE USE DISTANCE TO STORE THE VALUES IN THE MAP AND THEN WE ITERATE OVER THE INDEX DISTANCE AND PRINT THE VALUES
# [[9], [6, 7], [2, 3, 8, 1], [7, 11, 5, 1], [14, 12], [20]]
# this is inversal traversal
# this maintains the order if we send distance with map index we can actually solve the quetion
#  if not root:
#             return []
        
#         ans = defaultdict(list)  # {horizontal_distance: [(depth, value)]}
#         queue = deque([(root, 0, 0)])  # (node, horizontal distance, depth)
        
#         while queue:
#             size = len(queue)
#             for _ in range(size):  # Process all nodes at the current level
#                 node, hd, depth = queue.popleft()
#                 ans[hd].append((depth, node.val))  # Store (depth, value)
                
#                 if node.left:
#                     queue.append((node.left, hd - 1, depth + 1))  # Left child
#                 if node.right:
#                     queue.append((node.right, hd + 1, depth + 1))  # Right child
        
#         # Sorting by horizontal distance, then by (depth, value)
#         result = []
#         print(ans)
#         for key in sorted(ans.keys()): 
#             print(ans[key], key) 
#             ans[key].sort()  # Sort by (depth, value)
#             # 6 11 5 20 before sort as the depth and hd are same so we have to sort with values
#             # 6 5 11 20 now after sort
#             for i,val in ans[key]:
#                 # key=-1
#                 # ans=[-1:(a,b),(c,d)]
#                 # a==> depth
#                 # b==>root.val
#                 # i==> a
#                 # val==>b
              
#             result.append([val for i, val in ans[key]])  # Extract values
#             # [[6,5,11,20]]
        
#         return result
# from typing import Optional, List
# from collections import defaultdict, deque

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if(not root):
#             return []
#         ans=defaultdict(list)
#         queue=deque((root,0,0)) 
#         while(len(queue)>0):
#             size=len(queue)
#             for i in range(size):
#                 node,hd,depth=queue.popleft()
#                 ans[hd].append((depth,node))
#                 if(node.left is not None):
#                     queue.append((node.left,hd-1,depth+1))
#                 if(node.right is not None):
#                     queue.append((node.right,hd+1,depth+1))
#         result=[]
#         for key in sorted(ans.keys()):
#             ans[key].sort()
#             # apply sort in the tupple (depth,root.val) for making the correct order
#             result=[val for i, val in ans[key]]
#         return result
# Vertical Distance (dist) (Leftmost first)

# Depth (Level Order) (Topmost first)
# Value Order (Smaller values first if same depth & distance)
from typing import Optional, List
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        ans=defaultdict(list)
        queue=deque([(root,0,0)])
        # queue=[(root,0,0)]
        # root,hd,depth[root to that node path value tree height to that node]
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
            # sort by node value and depth if both are same mean ans[key] which is hd and depthe then value should be prioritiese
            result.append([val for i,val in ans[key]])
        return result


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(10)))
root.right = TreeNode(3, TreeNode(6), TreeNode(7, None, TreeNode(8)))

sol = Solution()
print(sol.verticalTraversal(root))