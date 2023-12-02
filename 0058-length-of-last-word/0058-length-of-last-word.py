class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=[];c=0;p=[]
        l=list(s.split(" "))
        for i in l:
            if i!="":
                p.append(i)
        return len(p[-1])
        