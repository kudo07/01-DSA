def hasPathSum(root,targetSum):
    if(root is None):
        return False 
    if(root.left is None and root.right is None):
        return root.val==target
    targetSum=targetSum-root.val 
    return haspathsum(root.left,targetSum) or haspathsum(root.right,targetSum)
# till root to leaf node and leaf node has no children
# so we have to minus till the leaf node and lead node val should be equal to the left target sum if the condition is satisfy
