class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l=[]
        for i in range(1,10):
            temp=i 
            for j in range(i+1,10):
                temp=temp*10+j 
                if temp>=low and temp<=high:
                    l.append(temp) 
        l.sort()
        return l
        
        