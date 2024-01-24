class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n=len(nums)
        p=[1]*n 
        for i in range(len(p)):
            p[(i-nums[i]+1)%n]-=1
        p=list(accumulate(p))
        return p.index(max(p))
        