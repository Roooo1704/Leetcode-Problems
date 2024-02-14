class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[];n=[];q=[];r=0;s=0
        for i in range(len(nums)):
            if nums[i]>0:
                p.append(nums[i])
            else:
                n.append(nums[i])
        for i in range(len(nums)):
            if i%2==0:
                q.append(p[r])
                r+=1
                if r==len(p):
                    continue 
            else:
                q.append(n[s])
                s+=1
                if s==len(n):
                    continue
        return q

        