class Solution:
    def firstUniqChar(self, s: str) -> int:
        l=[];p=[]
        for i in s:
            if i not in l:
                l.append(i)
        for i in range(len(l)):
            if s.count(l[i])==1:
                p.append(l[i])
        if len(p)==0:
            return -1
        else:
            a=list(sorted(s,key=s.count))
            b=a[0]
            for i in range(len(s)):
                if s[i]==b:
                    return i
                    break
                