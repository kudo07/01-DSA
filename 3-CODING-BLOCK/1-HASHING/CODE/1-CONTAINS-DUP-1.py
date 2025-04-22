def containsDuplicate( nums) :
    x={}
    for i in range(len(nums)):
        if nums[i] not in x:
            x[nums[i]]=1
        else:
            return True
    print(x)
    return False
    
nums=[1,2,1,2]
print(containsDuplicate(nums))