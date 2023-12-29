class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        m=[];n=[];c=0
        for i in range(len(s)):
            if s[i]=="#" and len(m)!=0:
                m.pop()
            elif len(m) == 0 and s[i] == '#':
                continue
            else:
                m.append(s[i])
        for i in range(len(t)):
            if t[i]=="#" and len(n)!=0:
                n.pop()
            elif len(n) == 0 and t[i] == '#':
                continue
            else:
                n.append(t[i])
        if m==n:
            return True
        else:
            return False
        