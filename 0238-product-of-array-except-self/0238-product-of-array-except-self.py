class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[];p=1;a=[];q=1;c=0
        for i in range(len(nums)):
            if nums[i]==0 and c==0:
                c=1
            else:
                p*=nums[i]
            q*=nums[i]
        for i in range(len(nums)):
            if nums[i]==0:
                a.append(p)
            else:
                a.append(q//nums[i])
        return a

        
        