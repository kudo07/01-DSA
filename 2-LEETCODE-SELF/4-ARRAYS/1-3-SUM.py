class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(0,len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                a=nums[i]
                b=nums[j]
                c=nums[k]
                if((a+b+c)==0):
                    ans.append([a,b,c])
                    while(j<k and nums[j]==nums[j+1]):
                        j+=1
                    while(j<k and nums[k]==nums[k-1]):
                        k-=1
                    j+=1
                    k-=1
                elif((a+b+c)>0):
                    k-=1
                elif((a+b+c)<0):
                    j+=1
        return ans

