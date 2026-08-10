class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p,s=1,1
        b=[1]*len(nums)
        for i in range(len(nums)):
            b[i]=p
            p*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            b[i]*=s
            s*=nums[i]
        return b
        
            