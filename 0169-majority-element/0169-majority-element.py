class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=[]
        b=set(nums)
        b=list(b)
        for i in range(len(b)):
            c=nums.count(b[i])
            a.append(c)
        d=max(a)
        for i in range(len(b)):
            e=nums.count(b[i])
            if e==d:
                return b[i]
                break
