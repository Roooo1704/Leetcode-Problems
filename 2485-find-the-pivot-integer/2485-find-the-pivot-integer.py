class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1,n+1):
            left=((i+1)*i)//2 
            right=(n*(n+1))//2-(i*(i-1))//2 
            if right==left:
                return i
        return -1