
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right =right

    
class Solution:
    def flatten(self,root):
        self.prev=None
        def recursePre(node):
            if(node is None):
                return 
            recursePre(node.right)
            recursePre(node.left)
            node.right=self.prev
            node.left=None
            self.prev=node
        recursePre(root)
    
def print_flattened_tree(root):
    while root:
        print(root.val, end=" -> ")
        root = root.right
    print("None")

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(5, None, TreeNode(6))

sol=Solution()
ans=sol.flatten(root)
print_flattened_tree(root)