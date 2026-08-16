class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c=1
        m=0
        s=set(nums)
        for i in s:
            if i-1 not in s:
                l=i
                c=1
                while l+1 in s:
                    l+=1
                    c+=1
                m=max(m,c)
        return m