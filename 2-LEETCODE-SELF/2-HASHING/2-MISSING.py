class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ=sum(nums)
        n=len(nums)
        total=n*(n+1)//2
        return total-summ
        