class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s=strs[0]
        m=len(s)
        e=strs[-1]
        n=len(e)
        i=0
        while(i<m and i<n):
  
            if(s[i]==e[i]):
                i+=1
            else:
               
                break
        return s[0:i] 
        