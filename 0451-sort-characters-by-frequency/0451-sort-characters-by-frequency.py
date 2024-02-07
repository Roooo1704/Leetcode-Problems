class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        l = sorted(list(set(s)), key=s.count, reverse=True)
        for i in l:
            ans += i * s.count(i)
        return ans\
        # l=[]
        # for i in s:
        #     l.append(i)
        # b=sorted(sorted(l,reverse=False),key=l.count)
        # b=sorted(b,reverse=True)
        # c="".join(b)
        # return c