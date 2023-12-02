class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=len(haystack)
        b=len(needle)
        if needle in haystack:
            if a==1 and b==1:
                return 0
            else:
                for i in range(len(haystack)-b+1):
                    if needle==haystack[i:i+b]:
                        return i
        else:
            return -1
            
        