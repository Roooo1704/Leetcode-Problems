class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=[];f=0
        a=sorted(nums,key=nums.count)
        a=a[::-1]
        l.append(a[0])
        nums.sort()
        for i in range(1,max(nums)):
            if i not in nums:
                l.append(i)
                f=1
                break
        if f==0:
            l.append(nums[len(nums)-1]+1)
        return l