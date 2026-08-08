class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        l=defaultdict(list)
        for i in strs:
            b="".join(sorted(i))
            l[b].append(i)
        return list(l.values())