class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        if y==y[::-1] and x>-1:
            return "true"
        