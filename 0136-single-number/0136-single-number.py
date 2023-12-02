class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=sorted(nums,key=nums.count)
        return a[0]