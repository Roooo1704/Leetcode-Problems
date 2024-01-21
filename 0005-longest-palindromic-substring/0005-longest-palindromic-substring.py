class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                a=s[i:j]
                if a==a[::-1]:
                    l.append(a)
        l.sort(key=len)
        return l[-1]

        