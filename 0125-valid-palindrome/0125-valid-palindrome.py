class Solution:
    def isPalindrome(self, s: str) -> bool:
        w=""
        a="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        for i in range(len(s)):
            if s[i] in a:
                w+=str(s[i].lower())
        if w==w[::-1]:
            return "true" 