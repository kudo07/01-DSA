class Solution:
    def balancedBt(root):
        def check(root):
            if(root is None):
                return 0
            left=check(root.left)
            if(left==-1):
                return -1
            
            right=check(root.right)
            if(right==-1):
                return -1
            
            if(abs(left,right)>1):
                return -1
            return max(left,right)+1
        return check(root)!=-1