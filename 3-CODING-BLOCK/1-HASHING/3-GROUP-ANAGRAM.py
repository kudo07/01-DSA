# tc:o(n*klogk)
# a=map(int,input().split(" "))
# for i in a:
#     print(i)

# a="ewfew"
# print(a.split())
a="rfgre"
print("".join(a))
print(a.split())
l=["1","3"]
print("@@".join(l))
# 1@@3
# rfgre

def groupAnagrams(strs):
    mp={}
    ans=[]
    for i in strs:
        sorted_str="".join(sorted(i))
        print(sorted(i))
        # sorted(i)== i.split("").sort()
        if(sorted_str in mp):
            ans[mp[sorted_str]].append(i)
        else:
           
            mp[sorted_str]=len(ans)
           
            ans.append([i])
  
    return ans
            

strs=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))