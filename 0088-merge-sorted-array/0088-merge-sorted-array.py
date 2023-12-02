class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        l=[]
        for i in range(m):
                l.append(num1[i])
        for i in range(n):
                l.append(num2[i])
        l.sort()
        num1[:]=l
        return num1