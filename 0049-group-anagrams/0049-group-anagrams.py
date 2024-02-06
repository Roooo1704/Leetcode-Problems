class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            f=str(sorted(i))
            if f not in d:
                d[f]=[]
            d[f].append(i)
        return list(d.values())
        