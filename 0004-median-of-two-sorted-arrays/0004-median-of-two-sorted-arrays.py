class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      l=nums1+nums2
      l.sort()
      if len(l)%2==0:
        a=l[(len(l)//2)-1] 
        b=l[(len(l))//2]
        return (a+b)/2
      else:
        b=l[len(l)//2]
        return b