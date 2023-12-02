class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0 and ((n > 0) and ((n & n - 1) == 0) and (n % 3 == 1)):
            return 1
        else:
            return 0
        