class Solution:
    def jump(self, nums: List[int]) -> int:
        left=0;right=0
        res=0;farthest=0
        while right<len(nums)-1:
            farthest=0
            for i in range(left,right+1):
                farthest=max(farthest,i+nums[i])
            left=right+1
            right=farthest
            res+=1 
        return res


        