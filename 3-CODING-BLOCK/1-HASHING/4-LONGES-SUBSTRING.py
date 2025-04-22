class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        ans=0
        j=0
        for i in range(len(s)):
            if(s[i] in mp):
                j=max(j,mp[s[i]]+1)
            mp[s[i]]=i
            ans=max(ans,i-j+1)
        return ans
        
       