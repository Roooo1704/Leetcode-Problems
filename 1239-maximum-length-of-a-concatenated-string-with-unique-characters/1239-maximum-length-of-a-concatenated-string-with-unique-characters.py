class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans=0;l=[]
        for i in range(len(arr)+1):
            l.extend(list(combinations(arr,i)))
        for i in range(len(l)):
            t="".join(l[i])
            if len(t)==len(set(t)):
                ans=max(ans,len(t))
        return ans
        