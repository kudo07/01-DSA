def levelOrder(self, root):
    if(not root):
        return []
    queue=[]
    ans=[]
    queue.append(root)
    ans.append(root.val)
    while(len(queue)>0):
        level=[]
        size=len(queue)
        for i in range(size)
            temp=queue.pop(0)
            if(temp.left is not None):
                queue.append(temp.left)
            if(temp.right is not None):
                queue.append(temp.right)
        if(queue):
            ans.append(queue[0].val)
    return ans