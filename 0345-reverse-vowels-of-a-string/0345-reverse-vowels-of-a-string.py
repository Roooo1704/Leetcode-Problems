class Solution:
    def reverseVowels(self, s: str) -> str:
        p=[];w="";a="aeiouAEIOU";q=0
        for i in range(len(s)):
            if s[i] in a:
                p.append(s[i])
        p=p[::-1]
        for i in range(len(s)):
            if s[i] not in a:
                w+=str(s[i])
            else:
                w+=p[q]
                q+=1
        return w
        