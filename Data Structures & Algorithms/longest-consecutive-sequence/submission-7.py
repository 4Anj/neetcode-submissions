class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c,m=1,1
        s=sorted(list(set(nums)))
        if not s:
            return 0
        l,r=0,1
        while r<len(s):
            if s[l]+1==s[r]:
                c+=1
                l=r
            else:
                m=max(m,c)
                c=1
                l=r
            r+=1
        return max(m,c)