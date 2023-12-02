class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x=n
        if (x and (not(x & (x - 1))) ):
            return 1
        else:
            return 0
        