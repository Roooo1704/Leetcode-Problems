class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sumi = 0; sumii = 0
        w=""
        for i in num1:
            a = int(i)
            sumi += a
            sumi *= 10
        sumi //= 10
        for i in num2:
            a = int(i)
            sumii += a
            sumii *= 10
        sumii //= 10
        res = sumi + sumii
        if res == 0:
            return '0'
        else:
            while res != 0:
                v = res%10
                w += str(v)
                res //= 10
            return w[::-1]
        