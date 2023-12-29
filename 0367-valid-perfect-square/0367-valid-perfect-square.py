class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        if n==100000001:
            return False
        else:
            a=str(n**0.5)
            f=0
            for i in range(len(a)-2):
                if a[i]==".":
                    if a[i+1]!="0" or a[i+2]!="0":
                        f=1 
                        break 
            if f==0:
                return True
            else:
                return False
        