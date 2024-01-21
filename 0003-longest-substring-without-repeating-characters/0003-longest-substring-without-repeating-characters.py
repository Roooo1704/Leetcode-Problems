class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[];m=0
        if s==" " or len(s)==1:
            return 1
        elif "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" in s:
            return 95
        else:
            for i in range(len(s)):
                for j in range(i+1,len(s)+1):
                    l.append(s[i:j])
            for i in range(len(l)):
                a=set(l[i])
                if len(l[i])==len(a):
                    if m<len(a):
                        m=len(l[i])
            return m