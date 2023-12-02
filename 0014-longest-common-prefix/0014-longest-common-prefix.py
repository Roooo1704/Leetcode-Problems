class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m=len(max(strs,key=len))
        p=[];q=[];s="";t=0;r=[];f=0
        ti=""
        if len(strs)==1:
            return "".join(strs)
        elif strs=="":
            return ""
        else:
            for i in range(len(strs)):
                if len(strs[i])!=m:
                    p.append(strs[i])
                else:
                    q.append(strs[i])
            for i in range(len(p)):
                c=p[i]
                n=m-len(c)
                d="*"*n
                c+=d 
                q.append(c)
            for i in range(m):
                r=[]
                for j in range(len(q)):
                    r.append(q[j][i])
                x=set(r)
                if len(x)==1:
                    f=1
                    s+=str(q[j][i])
                else:
                    f=0
                    break
            if s=="":
                return ti
            else:
                return s
        