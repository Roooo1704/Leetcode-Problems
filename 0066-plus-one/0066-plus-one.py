class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="";l=[]
        for i in range(len(digits)):
            s+=str(digits[i])
        a=str(int(s)+1)
        for i in range(len(a)):
            l.append(int(a[i]))
        return l
        