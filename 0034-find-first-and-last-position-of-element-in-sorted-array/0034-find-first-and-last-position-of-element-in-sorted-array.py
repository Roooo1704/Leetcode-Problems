class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[];b=0;a=0
        l.append(-1)
        l.append(-1)
        if target not in nums:
            return l
        else:
            a=nums.index(target)
            for i in range(a+1,len(nums)):
                if nums[i]==target:
                    b=i  
            if b==0:
                l.append(a)
                l.append(a)
                return l[2:]
            else:
                l.append(a)
                l.append(b)
                return l[2:]
        