class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            sort_s="".join(sorted(s))
            if sort_s in d:
                d[sort_s].append(s)
            else:
                d[sort_s]=[s]
        return list(d.values())