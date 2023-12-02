class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            if nums[i]<target:
                c+=1
            else:
                break 
        return c
            