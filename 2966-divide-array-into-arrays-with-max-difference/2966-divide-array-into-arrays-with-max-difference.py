class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        l=[];f=0
        nums.sort()
        for i in range(0,len(nums),3):
            l.append(nums[i:i+3])
        for i in range(len(l)):
            a=l[i]
            if abs(a[0]-a[2])<=k:
                f=1 
            else:
                f=0 
                return []
                break 
        if f==1:
            return l

                